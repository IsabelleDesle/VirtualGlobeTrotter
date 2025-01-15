using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Threading.Tasks;
using System;
using System.Linq;
using System.Collections;
using UnityEditor;

public class BuildImageReceiver : MonoBehaviour
{
    private TcpListener server;
    private bool isListening = false;
    private int port = 12345;
    public static bool imageReceived = false;
    
    private string resourcesPath;
    private string imagesPath;
    private string materialsFolderPath;
    private string[] previousFiles = new string[0]; // Initialize with empty array

    void Start()
    {
        #if UNITY_EDITOR
        resourcesPath = Path.Combine(Application.dataPath, "Resources");
        imagesPath = resourcesPath;
        materialsFolderPath = Path.Combine(resourcesPath, "Materials");
        #else
        imagesPath = Path.Combine(Application.dataPath, "..", "ReceivedImages");
        Directory.CreateDirectory(imagesPath);
        materialsFolderPath = Path.Combine(imagesPath, "Materials");
        Directory.CreateDirectory(materialsFolderPath);
        #endif
        
        // Create necessary directories
        Directory.CreateDirectory(imagesPath);
        Directory.CreateDirectory(materialsFolderPath);
        
        // Initialize previousFiles after directories are created
        previousFiles = GetImageFiles();
        
        StartServer();
        StartCoroutine(CheckForNewImages());
    }

    private string[] GetImageFiles()
    {
        if (!Directory.Exists(imagesPath)) return new string[0];
        
        return Directory.GetFiles(imagesPath)
            .Where(file => file.EndsWith(".png", StringComparison.OrdinalIgnoreCase) || 
                          file.EndsWith(".jpg", StringComparison.OrdinalIgnoreCase) || 
                          file.EndsWith(".jpeg", StringComparison.OrdinalIgnoreCase))
            .ToArray();
    }

    private IEnumerator CheckForNewImages()
    {
        while (true)
        {
            string[] currentFiles = GetImageFiles();
            var newFiles = currentFiles.Except(previousFiles ?? Array.Empty<string>()).ToArray();

            if (newFiles.Length > 0)
            {
                string newFile = newFiles.OrderByDescending(f => File.GetCreationTime(f)).First();
                string fileName = Path.GetFileNameWithoutExtension(newFile);
                Debug.Log($"New file detected: {fileName}");

                // Wait a bit to ensure the file is fully written
                yield return new WaitForSeconds(0.5f);

                #if UNITY_EDITOR
                AssetDatabase.Refresh();
                yield return new WaitForSeconds(0.5f); // Add additional wait for asset refresh
                #endif
                
                try
                {
                    // Create and load the texture
                    Texture2D newTexture = new Texture2D(2, 2);
                    byte[] fileData = File.ReadAllBytes(newFile);
                    
                    if (newTexture.LoadImage(fileData))
                    {
                        float aspectRatio = (float)newTexture.width / newTexture.height;
                        if (Mathf.Approximately(aspectRatio, 2f))
                        {
                            Debug.Log("Image loaded successfully.");
                            imageReceived = true;
                            
                            // Create and configure skybox material
                            Material skyboxMaterial = new Material(Shader.Find("Skybox/Panoramic"));
                            // DO NOT change this, it works in the editor
                            #if UNITY_EDITOR
                            newTexture = Resources.Load<Texture2D>(fileName);
                            #endif
                            skyboxMaterial.mainTexture = newTexture;
                            
                            #if UNITY_EDITOR
                            // Save the material as an asset in editor
                            string relativePath = $"Assets/Resources/Materials/{fileName}.mat";
                            AssetDatabase.CreateAsset(skyboxMaterial, relativePath);
                            AssetDatabase.SaveAssets();
                            AssetDatabase.Refresh();
                            // yield return new WaitForSeconds(0.5f); // Wait for asset refresh
                            
                            // Reload the material to ensure proper asset reference
                            skyboxMaterial = AssetDatabase.LoadAssetAtPath<Material>(relativePath);
                            #endif
                            
                            // Apply the skybox
                            RenderSettings.skybox = skyboxMaterial;
                            RenderSettings.skybox.SetFloat("_Exposure", 1f);
                            DynamicGI.UpdateEnvironment(); // Update lighting to reflect new skybox
                            
                            Debug.Log($"Skybox updated with new image: {fileName}");
                        }
                        else
                        {
                            Debug.LogWarning($"Image aspect ratio must be 2:1. Current ratio: {aspectRatio:F2}");
                        }
                    }
                    else
                    {
                        Debug.LogError($"Failed to load texture from file: {fileName}");
                    }
                }
                catch (Exception e)
                {
                    Debug.LogError($"Error processing image {fileName}: {e.Message}\n{e.StackTrace}");
                }
            }
            
            previousFiles = currentFiles;
            yield return new WaitForSeconds(1f);
        }
    }
    private async void ProcessClientAsync(TcpClient client)
    {
        try
        {
            using (NetworkStream stream = client.GetStream())
            {
                byte[] lengthBuffer = new byte[4];
                await stream.ReadAsync(lengthBuffer, 0, 4);
                int nameLength = BitConverter.ToInt32(lengthBuffer.Reverse().ToArray(), 0);
                
                byte[] nameBuffer = new byte[nameLength];
                await stream.ReadAsync(nameBuffer, 0, nameLength);
                string fileName = System.Text.Encoding.UTF8.GetString(nameBuffer);
                
                await stream.ReadAsync(lengthBuffer, 0, 4);
                int imageSize = BitConverter.ToInt32(lengthBuffer.Reverse().ToArray(), 0);
                
                byte[] imageBuffer = new byte[imageSize];
                int bytesRead = 0;
                while (bytesRead < imageSize)
                {
                    int remainingBytes = imageSize - bytesRead;
                    int chunk = await stream.ReadAsync(imageBuffer, bytesRead, remainingBytes);
                    if (chunk == 0) break;
                    bytesRead += chunk;
                }

                string savePath = Path.Combine(imagesPath, fileName);
                await File.WriteAllBytesAsync(savePath, imageBuffer);
                
                Debug.Log($"Image saved to {savePath}");
            }
        }
        catch (Exception e)
        {
            Debug.LogError($"Error processing client data: {e.Message}");
        }
        finally
        {
            client.Close();
        }
    }

    private void StartServer()
    {
        try
        {
            server = new TcpListener(IPAddress.Any, port);
            server.Start();
            isListening = true;
            Debug.Log("Server started. Listening for images...");
            
            ListenForImages();
        }
        catch (Exception e)
        {
            Debug.LogError($"Error starting server: {e.Message}");
        }
    }

    private void StopServer()
    {
        isListening = false;
        if (server != null)
        {
            server.Stop();
        }
    }

    private async void ListenForImages()
    {
        while (isListening)
        {
            try
            {
                TcpClient client = await server.AcceptTcpClientAsync();
                ProcessClientAsync(client);
            }
            catch (Exception e)
            {
                if (isListening)
                {
                    Debug.LogError($"Error accepting client: {e.Message}");
                }
            }
        }
    }
}