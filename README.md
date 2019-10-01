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
    'token' : TOKEN,
    'faceId' : faceId,
    'faceList': faceList
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
157.245.127.122:6978/detect   \
```json
headers: {
    'token' : TOKEN,
    'url' : faceId
}
```
\
Return:    
Okay 200:  
```json
{
    "faceId": "97868cf9-bb8e-4017-aeb3-ea602dd5f6b4"
}  
```
error\
bad API KEY\
403:  
```json
{
    "error": "bad token"
}
```
\
wrong headers  
401: \
```json
{
    "error": "bad"
}
```


-------------

