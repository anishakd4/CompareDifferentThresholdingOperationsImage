#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>
#include<iostream>

using namespace std;
using namespace cv;

Mat image, result;
int thresholdValue=150;
int maxValue = 255;
int thresholdType = 1;
int maxType = 4;

void onTrackbarChangeValue(int , void*){
    threshold(image, result, thresholdValue, maxValue, thresholdType);
    imshow("image", result);
}

int main(){
    image = imread("../assets/putin.jpg", IMREAD_GRAYSCALE);

    namedWindow("image", WINDOW_NORMAL);

    createTrackbar("Type", "image", &thresholdType, maxType, onTrackbarChangeValue);
    createTrackbar("Value", "image", &thresholdValue, maxValue, onTrackbarChangeValue);

    onTrackbarChangeValue(0, 0);

    while(true){
        int k = waitKey(10);

        if(k == 27){
            break;
        }
    }
    
    destroyAllWindows();
    return 0;
}