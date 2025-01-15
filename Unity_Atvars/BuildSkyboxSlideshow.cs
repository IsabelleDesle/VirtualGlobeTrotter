using UnityEngine;
using System.Collections;
using System.IO;
using System.Linq;
using System.Threading;
using System;

public class BuildSkyboxSlideshow : MonoBehaviour
{
    [SerializeField] private float slideshowInterval = 3f;
    private Material[] skyboxMaterials;
    private int currentIndex = 0;
    private bool isSlideshowRunning = true;
    private Coroutine slideshowCoroutine;

    // For fading the skybox
    // private Material blackSkybox;
    // [SerializeField] private float fadeSpeed = 2f; // Speed of the fade, can be adjusted in editor
    [SerializeField] public float fadeDuration; // Duration of the fade, in seconds
    int exposureID;

    void Awake()
    {
        // Creating a black skybox material for fading NO NEED FOR THIS
        // blackSkybox = new Material(Shader.Find("Skybox/Panoramic"));
        // blackSkybox.mainTexture = Texture2D.blackTexture;
        // Debug.Log("Black skybox created");

        // Loading the skybox materials that were included in the build
        skyboxMaterials = Resources.LoadAll<Material>("Materials")
            .Where(material => material.shader.name.Contains("Skybox"))
            .ToArray();
            
        if (skyboxMaterials.Length == 0)
        {
            Debug.LogWarning("No skybox materials found! Make sure they are in a Resources/Materials folder.");
        }
    }

    void Start()
    {
        exposureID = Shader.PropertyToID("_Exposure"); // Get the id of the exposure property for fading
        if (skyboxMaterials != null && skyboxMaterials.Length > 0)
        {
            RenderSettings.skybox = skyboxMaterials[0];
            slideshowCoroutine = StartCoroutine(RunSlideshow());
        }
        else
        {
            Debug.LogError("No skybox materials found! Slideshow will not run.");
        }
    }

    private IEnumerator RunSlideshow()
    {
        
        while (isSlideshowRunning && !BuildImageReceiver.imageReceived)
        {
            currentIndex = (currentIndex + 1) % skyboxMaterials.Length;
            RenderSettings.skybox = skyboxMaterials[currentIndex];
            DynamicGI.UpdateEnvironment();

            yield return StartCoroutine(FadeFromBlack());

            yield return new WaitForSeconds(slideshowInterval);
            if (BuildImageReceiver.imageReceived) 
            {
                // Set the skybox exposure to 1 in case it is set during the fade period
                break;
            }

            yield return StartCoroutine(FadeToBlack());

        }
        
        Debug.Log("Slideshow stopped - new image received");
    }


    private IEnumerator FadeToBlack()
    {
        Material currentSkybox = RenderSettings.skybox;
        float timer = 0;
        
        while (timer < fadeDuration)
        {
            timer += Time.deltaTime;
            // Lerping the skybox exposure from 1 to 0
            float newValue = Mathf.Lerp(1, 0, timer / fadeDuration);
            currentSkybox.SetFloat(exposureID, newValue);
            yield return null;
        }
        // Set the exposure back to 1, because otherwise the skybox will be black in next run
        currentSkybox.SetFloat(exposureID, 1);
    }

    private IEnumerator FadeFromBlack()
    {
        Material targetSkybox = skyboxMaterials[currentIndex];
        float timer = 0;
        
        while (timer < fadeDuration)
        {
            timer += Time.deltaTime;
            float newValue = Mathf.Lerp(0, 1, timer / fadeDuration);
            targetSkybox.SetFloat(exposureID, newValue);
            yield return null;
        }
    }

    public void RestartSlideshow()
    {
        if (slideshowCoroutine != null)
        {
            StopCoroutine(slideshowCoroutine);
        }
        
        BuildImageReceiver.imageReceived = false;
        isSlideshowRunning = true;
        slideshowCoroutine = StartCoroutine(RunSlideshow());
    }

    public void StopSlideshow()
    {
        isSlideshowRunning = false;
        if (slideshowCoroutine != null)
        {
            StopCoroutine(slideshowCoroutine);
        }
    }

    void OnDisable()
    {
        StopSlideshow();
        // Set the exposure back to 1, because otherwise the skybox will be black in next run
        RenderSettings.skybox.SetFloat(exposureID, 1);

    }
}