# hackxplore
## "Get nailed" : our submission for HACKXPLORE 2019

1. User uploads picture of their hand
2. If there's a hand in the picture, Hand Tracker will approve the user picture
  - *Hand Tracker code:*
  - *code for conditional acceptance:*
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
