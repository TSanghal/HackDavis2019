This project was developed during Davis's 2019 Hackathon for Social Good. My team and I decided to focus on the recent bouts of California wildfires, so we built a webpage that would inform users if they were located in areas with high risk of wildfires. 

To do this, we first built a sensor that read its surrounding temperature. Then, we created a simple webpage that asked the user to input their location. Using the Google Maps API, we found the closest sensor to this individual and read its data (this value was hardcoded because we only had one sensor). The data from the sensor was then used to determine whether or not the location was deemed safe or unsafe. 

In the future, a fully developed device might have sensors to take into account other conditions indicative of wildfires, like humidity and air quality. We might also use sophisticated machine learning algorithms and readings from multiple devices to create more accurate safety classifications.
