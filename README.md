# [QRowd](https://qrowdapp.herokuapp.com/)
#### *Crowd-sourced contact tracing powered by QR codes*
#### [Live Demo](https://qrowdapp.herokuapp.com/)
![1.png](/static/images/Screenshots/1.png)

## Inspiration
As we slowly readjust towards pre-pandemic life, it is essential to monitor the everyday interactions with others that may reinvigorate the Covid-19 virus. If we are not careful with the places we come and go, there is a great possibility that the pandemic will worsen. It is inevitable that the virus will spread without remembering where one came into contact with a Covid-19 positive individual. There is no doubt that we are all victims of the pandemic, indirect or direct. In order to return to a world without the hindrance of Covid-19, we must work together to prevent its further spread.

Contact tracing is a proven method to tackle Covid-19 at its source. By monitoring where individuals have been, both health officials and civilians can shut down infected locations before the virus spreads further. With citizens from all walks of life contributing to an crowd-source contact tracing application, new outbreaks can be suppressed easily. Not only will civilians be able to avoid areas infected by Covid-19 with contact tracing technology, but small businesses can also use the technology to make informed decisions about their own operation. Crowd-sourced contact tracing made simple is the future of public health technology.

## Functionality
There are two primary use cases for QRowd: civilians and local businesses.

After creating an account, users can immediately contribute to a worldwide contact tracing database. Now, every time a user visits a local business or public space, they can use their mobile device to scan the locations QR code. The user will then be prompted to enter their personal user ID. Using geocoding, the user's ID and location will be stored in a database for further reference. These locations are then used to populate an interactive contact tracing map, where a user can view the places they visited along with the times in which they were visited. Because the database is open-sourced, users can also use the map to view the activity at each location they visited, allowing them to determine whether or not they came into contact with a Covid-19 positive individual. However, because the only identification used is a randomly generated ID, user data is not compromised, ensuring complete privacy and security.

Local businesses can also take advantage of our platform by using it to make informed decisions about their own operation. Instead of creating a user account, local businesses simply request a QR code mapped to their location. Now, whenever a user scans the QR code, the local business will be notified, providing them with direct data regarding the customers and the places they may have come from. If a Covid-19 case is detected at the local business or at a location that one of their customers may have come from, the business may choose to shut down for a period of time, preventing the spread of the virus. Not only will this be beneficial for the business' brand and safety, but it will also protect their customers from falling victim to an infection.

![2.png](/static/images/Screenshots/3.png)

## Build Process
We used a Flask back-end powered by a MongoDB database, in conjunction with an HTML/CSS/Javascript front-end to build out QRowd. First, the web application framework was laid out by creating Flask routes corresponding to each page needed in the site on the app.py file. Within each route, we developed the needed back-end code. For example, within the scan route, which is where users are taken to upon scanning a QR code, contains a MongoDB URI connection that houses the user contact tracing database. After each scan, the corresponding location is appended to the list of locations under the user's ID number. The text input and success pages are implemented in the scan.html and scan_success.html pages, which utilize both CSS and Javascript to create an aesthetic UI/UX.

For the contact tracing map visualization feature (found in the map.html files) we utilize the Here API. After each scan, the corresponding location is appended to the list of locations under the user's ID number. This data is then accessed by the “map” route, where the location_list method retrieves the location_ids corresponding to a particular user, and the get_location method returns the longitude and latitude for each location. The frontend code is home to the data visualization component, which uses Here API to provide a live-feed contact tracing map that marks each user’s past locations. Using the MongoDB data from the Flask backend, we use Javascript to output a map containing markers on the user’s locations Finally, the HTML brings the rest of the front end together, creating an aesthetic, bootstrapped user interface.

## Challenges
The primary challenge that our team faced was the API connections needed for our data visualization feature. The first map API we used, MapBox, was extremely tough to use and led to extreme consequences in our code. Because most of the documentation was optimized for Javascript, it was difficult for us to create a http.client connection using Python. This caused us to have a hard time trying to implement the most important feature of the contact tracing app. Afterward, we tried to use the Google-Maps API via the gmplot library. However, it was difficult to find up to date documentation on the Python module, and as a result, we faced multiple circular import errors. Eventually, we were discovered Here API, which provided us with the map marking functionality that we needed.

![2.png](/static/images/Screenshots/2.png)

## What We Learned
Throughout the course of this project, we learned how to use map APIs to create a semi-real-time updating interface that shows locations that have been visited. We also learned how to create an interface with multiple NoSQL database collections to build a reusable and scalable web application. Moreover, we honed in on full-stack development techniques using Flask, allowing us to discover more about the framework behind a fully functional web application. Not only did we sharpen our technical skills, but QRowd also taught us many intangible skills, including contact tracing and other methods of combatting a pandemic.

We hope to continue learning more about the technical and social aspects of efficient contact tracing. During pandemics, it is important for people to have a grasp of their own health and welfare. As we prepare for the future, QRowd will help us continue playing our role in the fight against Covid-19.

## Requirements
Your machine will need flask, pymongo, json, geocoder, and dotenv to run this code. To get any of these libraries, you can just `pip install [insert library here]` in a terminal window. To run the code, first pull the github to your computer and then navigate to the folder where app.py is. Then open terminal and run the command `flask run`. This will direct you to a localhost website where you can interact with the product.

You will also need to to set up a `.env` file that houses all the API-keys that are specific to you. This will make the data available for you to use from your own account. The API-keys that are written up here are for one of our accounts that houses the data for our own app.

Copy the data below into the `.env` file and replace the information in the brackets with your API Keys and other data. See .env.sample for details.

```
ATLAS_URI={YOUR_ATLAS_URI_FROM_MONGODB}
FLASK_KEY={YOUR_FLASK_KEY}
```

## Setup:
1. Open command prompt
2. Install flask, pymongo, dns, json, and bson using `pip install [library name]`
3. Then download the github repo to your computer
4. Locate the repo in your file explorer
   -- Open command prompt from that folder's search bar by typing cmd into it
5. Then enter `flask run` in the command prompt
6. Copy the localhost link that is outputted and paste it into a web browser
7. Use the application in your browser


## What's Next for QRowd?
With Covid-19 showing little evidence of concluding soon, we have many plans to improve this application in the future. First, we would like to create a mobile app, providing people with a more seamless interaction with our web application. This would tie into the integration of a camera, allowing people to efficiently scan a QR code without ever having to leave the comfort of their mobile device. This will also remove the extra step of typing in location and user ID codes, which is only necessary in desktop environment. Finally, we would like to integrate a population heatmap into our application to allow people to avoid populated and crowded locations, reducing the risk of infection. Ultimately, with data filtration features on each map visualization, both businesses and individuals will be able to make informed decisions regarding the state of the pandemic.

## Youtube
https://youtu.be/-5CyrjfUMAQ

## Website
Click [here](https://qrowdapp.herokuapp.com/) to view the app for yourself!
