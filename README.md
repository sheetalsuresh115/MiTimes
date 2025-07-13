# MiTimes
Get and Post operations for Application Submission

1. Be able to run from the command line
2. Makes a request to 'https://au.mitimes.com/careers/apply/secret'
3. Post to 'https://au.mitimes.com/careers/apply'
   Method = "POST"
   Include 'Authorization' header with value from 2
   JSON formatted body with the following top level fields:
   name
   email
   job_title
   *final_attempt
   **extra_information

Print out the resultant HTTP status and response body to the command line
*Optional - On your final attempt submit with value of true.

**Optional - Add any additional fields to represent you in a JSON object, including but not necessarily limited to your relevant personal attributes, experience (whether on the job, or not), and why we should hire you.

We will email you upon a successful completion :)
