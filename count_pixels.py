PImage img;
boolean loaded;
 
void setup() {
  size(1482, 1482);
  img = loadImage("./output-files/nails_yellow.jpg");
  int cP = 0;
  loadPixels();
  int dimension = img.width * img.height;
  int y = img.width; 
  int x = img.height;
  for (int i = 0; i < dimension; i++) {
    color pxCl = pixels[y*width+x];
    if (pxCl == -3355444) {
      cP = cP+1;
    } else {
      cP = cP+0;
    }
  }
  println("Black pixels = " +cP);
  image(img, 0, 0);
}