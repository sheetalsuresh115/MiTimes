import requests

def get_authorization(url):
    try:
        response = requests.get(url)
        return response.json().get("result")
    except Exception as e:
        print(f"Error fetching {url}: {e}")


def post_application(url, token, payload):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        return response
    except requests.RequestException as e:
        print(f"Error posting application: {e}")


def main():
    get_url = "https://au.mitimes.com/careers/apply/secret"
    post_url = "https://au.mitimes.com/careers/apply"

    payload = {
        "name": "Sheetal Suresh",
        "email": "sheetalsuresh115@gmail.com",
        "job_title": "Senior Software Engineer",
        "final_attempt": True,
        "extra_information": {
            "years_of_experience": 9,
            "technical_stack": ["Ruby", "Ruby on Rails", "Python", "Django", "C#", "JavaScript", "SQL"],
            "strengths": ["Problem-solving", "Quick learner", "Self motivated"],
            "why_hire_me":
                 "I bring a mix of strong engineering skills and real-world experience across product teams. "
                 "I've worked at two product companies, where I built and maintained scalable applications" +
                 "and I'm currently contributing to research-driven solutions at the Industrial AI Research Centre. "
                 "I'm adaptable across tech stacks, quick to pick up new frameworks or languages and" +
                 " passionate about solving real-world problems through technology. "
        }
    }

    token = get_authorization(get_url)
    post_application(post_url, token, payload)


if __name__ == "__main__":
    main()
