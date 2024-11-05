> Agile Scrum!

Proof of concept for somebody else. -> think about recommendations if the original idea does not work.

> [!important]
> Communicate with the internal client at least once a week (one person per group)!

Atvars: Unity, 360 videos
Isabelle: organizational, backend(?)
Viola: UI/UX, web application(?)

ask Marie about requirements about the model's training.

> Some example models:
> music generator: [facebook/musicgen-melody · Hugging Face](https://huggingface.co/facebook/musicgen-melody)
> prompt enhancing with text2text: [gokaygokay/Flux-Prompt-Enhance · Hugging Face](https://huggingface.co/gokaygokay/Flux-Prompt-Enhance)
> image to video generator: [stabilityai/stable-video-diffusion-img2vid-xt · Hugging Face](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt)
> speech recognition: [openai/whisper-large-v3-turbo · Hugging Face](https://huggingface.co/openai/whisper-large-v3-turbo)

## Architecture

> [!example] Web application:
>
> - navigation screen with a start button;
> - world map (when a user chooses a region, a prompt is already beginning generating and if we need to use different locations at the different regions, the prompt is being modified);
> - a screen with a button to record voice input (which is enhanced and added to the prompt) and a cancel button to stop displaying.

> [!check] Backend & AI:
>
> - when the initial prompt is generated after choosing the location, the algorithm start:
>   1. Input the prompt into the image generator.
>   2. If we are not able to fine tune the image generator to output 360 view images, we need to somehow stich the images together seamlessly.
>   3. Feeding the adjusted prompt for sound to a music generator.
>   4. Feeding that image to an image to video generator.
>   5. Sending the output video and audio to the Unity part and save the video and the audio in a storage (in a volume if we are using containers).
> - when the voice input is made, the prompt is updated and the algorithm repeats itself (or if there are better ways to optimize it to not redo the whole prompt => would be useful).

Unity: Atvars:
Make an environment, add music

> [!danger] Possible challenges on the way
>
> - retraining and fine tuning the models to our needs: a lot of labeled data is needed, a lot of time is needed.
> - stitching the images together.
> - the application may be very slow due to a lot of generating that comes with it.
