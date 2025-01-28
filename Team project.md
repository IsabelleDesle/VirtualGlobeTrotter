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
researching ai pipeline: webservice=>voice input=>json file=>database=>path added in json file =>unity=>reads periodically the json file=>show assets in path in json file in immersive room 

test in immersive room: Thursday 09/01 - 10:30. Meeting at immersive room. project on USB stick -> rescheduled for Friday 10:30.

09/01/2025
morning brief:
- Isabelle: working on the AI Pipeline class - database part. Getting the string from the API and searching throught the database for the appropriate enviroment, outputting a path to the folder where the images can be found. Couple of options for getting an output: 
    - random folder path based on the continent(the initial environment, shown in the immersive room after selecting the continent) (should be a separate function); 
    - specific folder path based on the voice input: searching through a database using the input from a child. If the relevance of the search is close to zero, then we generate new images by using the AI pipeline code.

- Viola: starting creating the AI pipeline code by using the models that Atvars provided.

- Atvars: working on changing the images in the environment using code.

github virtual globetrotter for everything concerning the project i.e. the code, presentations, emails, meeting notes. 

08/01/2025
- meeting with Nathan Segers: 
    - immersive room needs a 5G adapter for internet. Tom Decavele will join us Friday at 10:30 in the immersive room 
    - pc in immersive room will connect with our laptop or vm via internet. 
    - Using the howest VPN it is possible to contact the pc from outside howest. So the generated images can be tested on the pc
    - we can make use of the comfy Ai script from Devine to make images. Videos are not doable 
    - the comfy script contains positive and negative prompt but also the adjustment to the needed size and resolution.     
- plan a first meeting with ergo next week. 
- Ai pipeline needed: to define how data transfer from webservice (flask)=> voice input for database (elastic search) or generate image=> unity => immersive room 
scenario: 
    1/ the child is in the immersive room and clicks on a continent (South-America, North-America, Europe, Asia-Middle-East, Oceania, Africa)
    2/ an image is chosen randomly based on the chosen continent
    3/ the child can ask for another image with voice input
    4/ voice input = a string
    5/ database elastic search is addressed to find relevant image based on continent + voice input
    6/  if relevance > 0, images are shown in immersive room
        else: new image is generated based on continent + voice input. In meantime the current image is still shown. 
    7/ go back to 3/
- using docker for ElasticSearch
- images need to be generated on beforehand. The more images we have the better. Account and access token needed on hugging face.


09/01/2025
- make a Ai pipeline
- unity research 
- pregenerate images (make account/key + pull github first)

Friday 10/01/2024
- test in immersive room with Thibaut, Tom De cavele, Viola, Isabelle and Atvars to connect pc immersive room to internet.
- internet needed to get the image to show in imm.room. 5g adapter needed that's why Tom is also present.

  during test: ethernet is added, no need for the 5g adapter anymore. 
- the laptop will have to make connection to the pc of the imm room using a static ip and the same network as the pc.
did't work but image can be tested: the resolution must be higher. 8k by wall, not for the entire image.
ethernet connection will be fast enough for this. Some installation has to be done in the unity application

- to do : make docker work, run elastic search and python in docker. 


Monday 13/01/2024

connect pc immersive room to laptop's ip address and laptop uses docker to access elastic search 
or to generate new images. This can not be done in docker as its allocated space is limited. 
asking Thibaut and Nathan how to connect. Have to be on the same network (not eduroam)

to do : needed 1 app.py file to use invoice input (if none then use "random") and to output a path to an existing image 
or to start the image generator to generate a new one using AI : in meantime show a slideshow of existing images. 

negative prompt can be used to exclude profanity 
assignment P2P for first week: too late to upload but no grading for this. Friday it counts for 10%

show images in a slideshow while waiting the generation of new image (space bar necessary? no use of keyboard is better )

Atvars researches the text to audio part and further unity 
2morrow 14/01: test the immersive room with generated images to see if impainting is okay 

to test python file without running in docker 

Tuesday 14/01
- search and generate image works, docker only for elastic search
- incorporate searching in db into the class of the environmentgeneration and run the whole ai line on 1 laptop
- images are inpainted using other model.
- testing in imm room: the connection works but laptop and pc of imm room: firewall needs to be disabled. 
- unity doesn't show new image
- resolution is a lot better

 Wednesday 15/01
 - prepare presentation based on introduct.week
 - prepare demo for friday:
 -    * start docker on 1 laptop
      * access elastic search on laptop 2 + webservice, register voice input and continent search in elastic search,
      * based on relevance create new image, inpaint and upscale and send to laptop3
      * unity runs on laptop 3 and shows new image. in meantime show slideshow;
  - film the demo in case a lve demo is not possible in presentation Friday.
  - define a scenario on beforehand: which continent & voice input for existing image and what voice input for new image. 
  - prepare document functional analysis, based on doc of intro week.
  - unity change to receive and show new image. images don't need to be saved in unity folder. 
  - audio need to be added later

Thursday 16/01
- finish the presentation & doc functional analysis 
- improve relevance of found images
- research ai model for audio
- prepare and design doc
  
- images in unity:
   -  import images = 12345 port:
   Automatically creates and saves the Skybox material,
   which means that an image sent to this port
   will be included in the slideshow when the project is run afterwards.
   - show images: 12346 port:
   For just showing the images.
   Works both in Unity editor, and in production.
   Does not save the images

Friday 17/01
- 10:30 presentation in Penta 
- 13:30 test in imm room

Monday 20/01
- test in imm room at 10:00
- some images show edges, other are not shown completely 
improvement of elastic search queries: and operator added to search for all the words, 
stop words are not taken into account, higher score for field title than for field content, 
boost score if phrase in query is found completely, relevance threshold = 8, fuziness 1,
no fuziness for searching phrase. 
- fun facts on the image: no func facts anymore, instead 8 or more CTAI robots will be shown in a image
during the generation of a new image. The viewer is asked to search the 8 CTAI robots while waiting
no slide show will be shown during waiting.
- audio ambient sound : category Nature, City, Ocean, City, Underwater, Wind
  filename format = nature-sheep in a meadom.jpg, underwater-coral reef.jpg
- webservice is accessible via mobile phone, layout is consistent and pretty
- prompt need to be better to generate more realistic images of animals
- final test with IlseMeerschaert, Laura Kyndt, Marie, Thibaut, Jordy, Charlotte Larmuseau planned Friday 24th

Tuesdag 21/01: 
- prompt enhancing
- audio
- robot on random places in image
- image creation must be ready Thursday, inclusive the csv with the content
- for now category for audio will be added manually, a random sound is used for on the spot generated images.
- fix on map website  

Wednesday 22/01
Ingenix to run website. To mention in installation guide. 
at 11:00 imm room meeting for audio test 
Connect game to backend of website
Other todo’s in Trello : 
Fun facts: became find the robot game (test it today)
Fill the csv . 
Map is fixed
Pregenerate images (ids) put them on a own own drive in folder image/asia en share the folder on teams. Name csv images_path_isabelle. 

Clean code (ids) env generator; erase the comments except explain what the code does. Between ‘’’      ‘’’ 
But read the file, or calculate the number and other repetitive things delete
Remove repetitive things too. Head and tail can be deleted too, because not used anymore. 

Github organization (ids).
Main thing now: pregenerate images.connecting everything
Put the 
Inpainting image nice to have maybe. 
TO DO: Nice to have: category. Text to txt model: gemma 2 b to enhance prompt. Put propmpt in there, based on this sentence, choose the category that is appropriate. 

FROM FRIDAY presentation and documents, user manual and installation guide, retrospective. P2P due on evening Tuesday. . look at the assignments 

Functional analysis this weekend adjust and add (ids)
Monday installation guide. On Monday and Tuesday at Markebekestraat

23/01
test in imm room at 14:00 with Jordy. This is the last test before the test with Ilse M on Friday. 
images must be available in the database: monuments, animals and landscapes. 
Marvel and comic book, and cartoon images are more difficult

An A4 with tips for voice input should be available in the imm room : 
be specific and detailled. not just "animal" but "giraffe in the forest"
not just "rome" but "colloseum in Rome on a sunny day"
not just "beach" but "beach, sun, blue ocean and palm trees"

the friendliness of AI: 
AI will generate images of animals in natural environment rather than in a zoo.
AI will generate images of dolphins in an ocean rather than in a dolphinarium
AI will generate images of free birds instead of caged ones. 
AI will not generate cartoon, game or film characters to respect the creator (designer conduct)

meeting at the HQ at  12:30. 
isabelle: images of Africa + monuments in Belgium, try zoo
Atvars: Australia: the same 
viola: South and North America
Atvars will also be working on UI and unity today
Viola and Isabelle: implement the random voice input concept this afternoon

24/01/2025
- no images need to be created from now on. 

from now focus on presentation, documents, user manual, installation guide
- ppt is on one drive.
- this weekend each of us thinks about what we want to talk about in 3 minutes.
- before the presentation: start the laptop and the video
- book a immers room test on Monday. preferable in the morning.
- monday afternoon: rehearsel of the presentation .

- viola: installation guide, design doc
- atvars: unity part
- isabelle: functional analysis. all technical explanations that are now in the presentation
  must be transferred in the functional analysis. + use manual and installation guide.

retrospective (ok)
  
Documents to hand in: 
1/Presentation (PDF)
Brief introduction of the project (content + technical approach)
Scrum conclusion (not a weekly review, but a summary including the sprint backlogs, retrospectives, and time tracking)
WHY IS YOUR PROJECT IMPORTANT. WHAT DO THE CUSTOMER WANT? HOW DID YOU SOLVE IT? 
no technical explanation. keep it high level: we used a special software unity for..., after researching a lot of possibilities we used Elastic searhc as database because of the full text search to find existing images corresponding to the input. 

2/ Final version of the Functional Analysis  (PDF)
Problem definition and proposed solution, target audience analysis, comparison with existing solutions, core MVP features, user flow diagrams, wireframes, and results from user testing.
(Includes updates based on additional user test information and iterations after the interim evaluation.)

3/ Final version of the Design Document (PDF)

4/ User Manual for the Client (PDF)
(This manual should enable the user to get started with the solution.)

5/ Installation Guide (technical aspect) (PDF)
(Explains how the client can set up/install the project and get it running.)
Zip file containing the project source code (ZIP)

27/01/25
- 10:00 : immersive room to record the project to show during presentation and as plan b for live demo. 
- working on documents: user manual, installation guide, functional analysis, design document and poster

28/01/25
- making the presentation. Adding the video.
- Preparing the text and timing it to divide speaking time equally
- make the zip for the source code (after short meeting with frederik).
- poster is ready to print in howest 
  
