I used IBM Watson Assistant (formerly known as Watson Bluemix). The free-tier IBM account gave me access to a sandbox environment for making a dialogue agent with the Watson platform. The docs / getting-started walkthrough were very thorough, and I was able to make a pretty good dialogue agent in an hour or so.

Last semester, I worked with the team that manages BYU's live-chat system on their main website. Since a lot of the questions through this service are predictable, I thought this would be a cool use case for implementing a dialogue agent. 

The most asked questions on the BYU chat platform are about tuition, parking, and admissions -- so I decided this would be the focus of my dialogue agent. The Watson Assistant uses "Intents" and "Dialogs". The Intents are used to determine what is being said by the user, and the Dialogs are used to respond. So for questions about parking, I defined an Intent called #tuition, which used "how much is tuition at BYU" as an example sentence. I them made a Dialog that looked for #tuition Intents, and responded with "Tuition at BYU is...". At first I didn't see how this approach was different than a hard-coded script, but I found out that the Watson platform is pretty smart in how it handles questions. By using the interactive chat feature, I tested many variations of asking for tuition, and 9 times out of 10, Watson correctly identified the Intent. When the Intent was not correctly found, I was able to train the model by selecting the intended Intent.

I added other Intents and Dialogs and continued to play around with the system. I was surprised at how well it worked. Compared to OpenDial (which I downloaded and experimented with for ~10 min), Watson Assistant was super easy to use and was extremely flexible in understanding user input. I'm not sure how much the production version of the platform costs, but I would definitly consider it if I had a future use for a dialogue agent. 

Screenshots:
* [apply.PNG](apply.PNG) -- testing how well the agent handled a statement + question
* [general.PNG](general.PNG) -- showing off some of the basic dialog that comes pre-built
* [menu.PNG](menu.PNG) -- example of the interface used to create Intent/Dialogs
* [parking.PNG](parking.PNG) -- example of Watson Assistant handling different questions of similar intent
* [training.PNG](training.PNG) -- correcting the Assistant by selecting the correct Intent