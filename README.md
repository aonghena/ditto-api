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
    "token" : TOKEN,
    "faceId" : faceId,
    "faceList": faceList
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
    "faceRectangle": {
      "top": 74,
      "left": 40,
      "width": 111,
      "height": 111
    },
    "faceLandmarks": {
      "pupilLeft": {
        "x": 67.4,
        "y": 109
      },
      "pupilRight": {
        "x": 115.8,
        "y": 99.2
      },
      "noseTip": {
        "x": 93.2,
        "y": 137.8
      },
      "mouthLeft": {
        "x": 79.2,
        "y": 158.4
      },
      "mouthRight": {
        "x": 124.4,
        "y": 149
      },
      "eyebrowLeftOuter": {
        "x": 49.9,
        "y": 101.3
      },
      "eyebrowLeftInner": {
        "x": 77.1,
        "y": 97.1
      },
      "eyeLeftOuter": {
        "x": 58.9,
        "y": 111.6
      },
      "eyeLeftTop": {
        "x": 66.5,
        "y": 106.2
      },
      "eyeLeftBottom": {
        "x": 67.4,
        "y": 112
      },
      "eyeLeftInner": {
        "x": 75.4,
        "y": 109.6
      },
      "eyebrowRightInner": {
        "x": 100.3,
        "y": 93.1
      },
      "eyebrowRightOuter": {
        "x": 131.9,
        "y": 88.7
      },
      "eyeRightInner": {
        "x": 107.7,
        "y": 102.1
      },
      "eyeRightTop": {
        "x": 114.7,
        "y": 97
      },
      "eyeRightBottom": {
        "x": 115.8,
        "y": 102.1
      },
      "eyeRightOuter": {
        "x": 122.8,
        "y": 98.9
      },
      "noseRootLeft": {
        "x": 83.9,
        "y": 107.8
      },
      "noseRootRight": {
        "x": 97.2,
        "y": 105.3
      },
      "noseLeftAlarTop": {
        "x": 83.1,
        "y": 128.9
      },
      "noseRightAlarTop": {
        "x": 106.1,
        "y": 125.9
      },
      "noseLeftAlarOutTip": {
        "x": 79.6,
        "y": 138.8
      },
      "noseRightAlarOutTip": {
        "x": 110.9,
        "y": 133.7
      },
      "upperLipTop": {
        "x": 99,
        "y": 152.7
      },
      "upperLipBottom": {
        "x": 99.7,
        "y": 156.1
      },
      "underLipTop": {
        "x": 101.6,
        "y": 162
      },
      "underLipBottom": {
        "x": 103.1,
        "y": 168.3
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