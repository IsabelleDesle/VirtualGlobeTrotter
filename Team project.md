# VirtualGlobeTrotter
Team Project Virtual GlobeTrotter

----------
07/11/2024 afternoon : Meeting Frederik, Viola, Atvars and Isabelle 
Don't define your week 3 and 4 sprints
Sprints should be filled only for the next week.
 
Beside that everything looks good.
It's important that when it's in progress, someone is linked to the card.
For future, it doesn't really matter who does what.
 
It's okay if the project manager Ergo don't respond now.
We can add the questions in Trello, which we have done already.
 
It's okay to just have images.
The outcome is not the most important thing.
 
>When you generate something with ai, it will be unrealistic. Does it need to be realistic?
>Frederik : not very important that it is educationally completely correct (kangaroos around the pyramids)
If anything, it's better for the kids, and it encourages creativity.
 
The database should not be in the cloud, that's perfect.
 
Do we index with Lucene?
Maybe don't use MYSQL. Don't think about it now, it's okay to not know this yet.
Probably SQL is not the best option, but the question stays open. Frederik will ask Wouter, but for the Proof of Concept, we can use SQL.
SQL has full text search, but the way of querying is different.
It's only 3 weeks, don't do anything crazy. If it's a few prompts, use SQL.
 
Assignment extended to 18:30
---- 


06/11/2024 evening
added on github: 
presentation version 1 
gitignore 
example photo to provide path in database
sql script

-------

meeting Viola, Atvars and Isabelle 
04/11/2024 afternoon

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

06/01/2025 week 1 
every day meeting at 9:30. 
on the spot creation of images is not a must 
a meeting with the customer needs to be planned (cf mail)
full text search in mysql okay using transcription of invoice input to text

07/01/2025
the concept : 
pretrained images/animations/videos will be used. 
training on the spot is option due to constraint time and costs. 

using json format to connect applications
merge webservice repo into to other
researching ai pipeline: webservice=>voice input=>database=>images or path =>unity=>immersive room 

test in immersive room: 08/01 - 10:30. Meeting at immersive room. project on USB stick




