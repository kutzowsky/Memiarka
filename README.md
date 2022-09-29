# Memiarka

AWS serverless API for generating meme(s) like this one below + some basic frontend to use it.

![Sample meme image](https://raw.githubusercontent.com/kutzowsky/Memiarka/main/sample.png)

There are some moments in life when Angry Pingu is my spirit animal. When those moments combine with the desire to learn Pillow library and some AWS - this happens.

## How to use it?

### I just want to run it

Deployed version should be available [here](https://memiarka.kopytny.ninja). (Warning, some polish ahead, but you'll manage.)

### I want to deploy it myself

Frontend is just static webpage, so anything which can serve some HTML with JS and some CSS would be ok.

Backend can be deployed to AWS using SAM CLI using:

`sam build --use-container`

`sam deploy --guided`

Hovewer, some manual tweaks are required. See **Known issues and limitations** section.

There's an option to run and test it locally. Please refer to [SAM documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html).

## How it works

1. Frontend does GET call with two meme text lines, e.g.:
`https://API.URL/function?firstLine=Chmura?&secondLine=A na co to komu?`

1. Call goes to the API Gateway which forwards it to Lambda function

2. Lambda function gets meme template and font from `INPUT_BUCKET`, uses Pillow to add meme text and then saves it to `OUTPUT_BUCKET`.

3. Caller gets URL to the produced image in JSON response.
```json
{"memeUrl": "https://OUTPUTBUCKET.s3.amazonaws.com/93869b4a-d57e-4c00-a06a-7ca471de721c.png"}
```

## Requirements

* Python,
* [Pillow](https://pillow.readthedocs.io/en/stable/),
* AWS account,
* [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).

## Known issues and limitations

Because project is still in development, there are some loose bits and pieces:

* only Angry Pingu memes are supported right now,
* error handling in backend code improvement.

Things that needs to be done manually:

* `API_URL` in frontend's `app.js`,
* input and output bucket creation,
* input bucket needs to be populated with `backend/static` directory contents,
* output bucket objects need to be public,
* setting [object lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) for output buckets is recommended,
* lambda execution role permissions to buckets mentioned above,
* `INPUT_BUCKET` and `OUTPUT_BUCKET` environment variables for lambda function (bucket names, not ARNs),
* update CORS allow origin in lambda code.
  
... and that's all. Sorry, still learning SAM and CloudFormation.

## Trivia

Memiarka is made up polish word which can mean meme generator (person or machine, female). For example, there is kucharka - female cook, tokarka - lathe and kolarka - female cyclist or sometimes road bike (depending on the context). Learn polish, it's fun!