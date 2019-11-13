# ditto-api

  
### HEALTH 

\
Use to check health of API  \
157.245.127.122:6978/health - checks health  

------------
 
 ### FIND  
\
157.245.127.122:6978/find 
```json
headers: {
    "token" : "TOKEN",
    "faceId" : "faceId",
    "faceList": "faceList"
}
```
  \
Return:  \
Okay 200:
```json
[
    {
        "persistedFaceId": "1b58de70-d6c5-422e-9d49-40b600e1d464",
        "confidence": 0.36
    },
    {
        "persistedFaceId": "3e2ddb0d-98fb-4ed4-84aa-aae831bcce73",
        "confidence": 0.25359
    },
    {
        "persistedFaceId": "f8ef8a9c-3a12-4147-ac58-08b33f0cf89b",
        "confidence": 0.2529
    },
    {
        "persistedFaceId": "fd2e92b4-8d0e-4881-aa40-4eb16d1f4d0a",
        "confidence": 0.23788
    },
    {
        "persistedFaceId": "50f80a10-41b5-43cc-9cf9-5e607cc1bbb4",
        "confidence": 0.23646
    },
    {
        "persistedFaceId": "5d509115-5e66-46bd-baa2-51967c561a09",
        "confidence": 0.22896
    },
    {
        "persistedFaceId": "32ee81d6-6f2c-4afb-b0d5-a8644d5c160e",
        "confidence": 0.22241
    },
    {
        "persistedFaceId": "b39f1266-eae5-4d9f-88f9-aed7c99ee08c",
        "confidence": 0.21036
    },
    {
        "persistedFaceId": "8e24e635-9e14-48e1-9e15-4e31137dee52",
        "confidence": 0.20391
    },
    {
        "persistedFaceId": "012359bd-df41-4ea6-9a17-aaf9d753676f",
        "confidence": 0.20325
    }
]
```
error  \
bad API KEY  \
403:    
```json
{
    "error": "bad token"
}
```
\
Wrong Headers  
```json
{
    "error": {
        "code": "CODE",
        "message": "MESSAGE."
    }
}
```

---------------
### DETECT  
\
157.245.127.122:6978/detect   
```json
headers: {
    "token" : "TOKEN",
    "url" : "faceId"
}
```
\
Return:    
Okay 200:  
```json
[
    {
        "faceId": "abec4370-04f2-416a-a351-22999040ffed",
        "faceRectangle": {
            "top": 485,
            "left": 310,
            "width": 873,
            "height": 873
        },
        "faceLandmarks": {
            "pupilLeft": {
                "x": 538.5,
                "y": 763.9
            },
            "pupilRight": {
                "x": 929.5,
                "y": 701.2
            },
            "noseTip": {
                "x": 713.7,
                "y": 972.1
            },
            "mouthLeft": {
                "x": 576.4,
                "y": 1134.7
            },
            "mouthRight": {
                "x": 983.2,
                "y": 1082.4
            },
            "eyebrowLeftOuter": {
                "x": 372.9,
                "y": 709.4
            },
            "eyebrowLeftInner": {
                "x": 607.6,
                "y": 677.1
            },
            "eyeLeftOuter": {
                "x": 479.7,
                "y": 780.7
            },
            "eyeLeftTop": {
                "x": 529.8,
                "y": 748.6
            },
            "eyeLeftBottom": {
                "x": 535.9,
                "y": 793.9
            },
            "eyeLeftInner": {
                "x": 593.2,
                "y": 767.3
            },
            "eyebrowRightInner": {
                "x": 767.5,
                "y": 659.8
            },
            "eyebrowRightOuter": {
                "x": 1057.0,
                "y": 607.5
            },
            "eyeRightInner": {
                "x": 855.0,
                "y": 717.3
            },
            "eyeRightTop": {
                "x": 904.5,
                "y": 683.6
            },
            "eyeRightBottom": {
                "x": 908.4,
                "y": 727.6
            },
            "eyeRightOuter": {
                "x": 968.2,
                "y": 699.5
            },
            "noseRootLeft": {
                "x": 649.9,
                "y": 763.1
            },
            "noseRootRight": {
                "x": 754.8,
                "y": 743.1
            },
            "noseLeftAlarTop": {
                "x": 634.9,
                "y": 900.1
            },
            "noseRightAlarTop": {
                "x": 805.5,
                "y": 882.0
            },
            "noseLeftAlarOutTip": {
                "x": 603.6,
                "y": 973.3
            },
            "noseRightAlarOutTip": {
                "x": 877.3,
                "y": 941.1
            },
            "upperLipTop": {
                "x": 759.4,
                "y": 1092.8
            },
            "upperLipBottom": {
                "x": 765.6,
                "y": 1126.2
            },
            "underLipTop": {
                "x": 777.5,
                "y": 1170.4
            },
            "underLipBottom": {
                "x": 784.2,
                "y": 1221.2
            }
        },
        "faceAttributes": {
            "smile": 1.0,
            "headPose": {
                "pitch": -0.3,
                "roll": -12.0,
                "yaw": -6.5
            },
            "gender": "male",
            "age": 56.0,
            "facialHair": {
                "moustache": 0.1,
                "beard": 0.1,
                "sideburns": 0.1
            },
            "glasses": "ReadingGlasses",
            "emotion": {
                "anger": 0.0,
                "contempt": 0.0,
                "disgust": 0.0,
                "fear": 0.0,
                "happiness": 1.0,
                "neutral": 0.0,
                "sadness": 0.0,
                "surprise": 0.0
            },
            "blur": {
                "blurLevel": "low",
                "value": 0.07
            },
            "exposure": {
                "exposureLevel": "goodExposure",
                "value": 0.74
            },
            "noise": {
                "noiseLevel": "high",
                "value": 0.83
            },
            "makeup": {
                "eyeMakeup": false,
                "lipMakeup": false
            },
            "accessories": [
                {
                    "type": "glasses",
                    "confidence": 0.99
                }
            ],
            "occlusion": {
                "foreheadOccluded": false,
                "eyeOccluded": false,
                "mouthOccluded": false
            },
            "hair": {
                "bald": 0.06,
                "invisible": false,
                "hairColor": [
                    {
                        "color": "brown",
                        "confidence": 0.99
                    },
                    {
                        "color": "gray",
                        "confidence": 0.7
                    },
                    {
                        "color": "black",
                        "confidence": 0.57
                    },
                    {
                        "color": "blond",
                        "confidence": 0.21
                    },
                    {
                        "color": "red",
                        "confidence": 0.11
                    },
                    {
                        "color": "other",
                        "confidence": 0.06
                    }
                ]
            }
        }
    }
]
```
error\
bad API KEY\
200:  
```json
{
    "error": "bad token"
}
```
\
wrong headers  
401: 
```json
{
    "error": {
        "code": "InvalidURL",
        "message": "Invalid image URL."
    }
}
```
---------------
### DETECT1  
\
157.245.127.122:6978/detect1   
```json
headers: {
    "token" : TOKEN,
    "url" : faceId
}
```
\
Return:    
Okay 200:  
```json
[
  {
    "faceId": "f51c2640-ca02-4e0c-a1eb-5ce6599e52a2",
  }
]
```
error\
bad API KEY\
200:  
```json
{
    "error": "bad token"
}
```
\
wrong headers  
401: 
```json
{
    "error": {
        "code": "InvalidURL",
        "message": "Invalid image URL."
    }
}
```
-------------