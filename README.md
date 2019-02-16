# hackxplore
## "Get Nailed" : our submission for HACKXPLORE 2019

We created the "Get Nailed" app with our potential consumers in mind - they can easily use our app for early diagnosis of anemia, fungal infections or potential oxygen-deprivation related diseases. The app uses the Object Detection API Tensorflow (https://www.tensorflow.org/) to detect user's hands and isolate images of their nails. Our code then looks through the image files for RGB values that correspond to the colour of nails of people with anemia, fungal infections and those who lack oxygen.

1. User uploads picture of their hand
2. If there's a hand in the picture, Object Detection will approve the user picture
  - *Object detection*
3. detect_color files will use diseased nails RGB values --> extract those RGB values and create an image
  - *code for detecting yellow nails*
  - *code for detecting light pink nails*
  - *code for detecting blue nails*
  - *code for detecting black nails*
4. From output image -> count number of coloured pixels
5. Coloured pixels / # of total pixels -> resulting % is used to 'diagnose'
6. If diagnosed, refers to a list of nearby doctors
    - *code for counting number of non-black pixels, calculating % and diagnosis*
    - *code for referring to doctors* 
