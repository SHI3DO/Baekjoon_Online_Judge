import requests
from bs4 import BeautifulSoup

request_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), }


def get_baekjoon(num):
    base = 'https://www.acmicpc.net/problem/'
    url = base + num

    response = requests.get(url, headers=request_headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        problem_description = soup.select('#problem_description > p')
        problem_ul = soup.select('#problem_description > ul')
        input_description = soup.select('#problem_input > p')
        output_description = soup.select('#problem_output > p')
        try:
            sample_input = soup.select_one('#sampleinput1').text.strip()
        except Exception as e:
            print(e)
        try:
            sample_output = soup.select_one('#sampleoutput1').text.strip()
        except Exception as e:
            print(e)
        sample_i = soup.select("pre[id^=sample-input]")
        sample_o = soup.select("pre[id^=sample-output]")

        return_text = ""

        return_text += f"#####   Problem {num}  ######" + "\n"
        for i in problem_description:
            try:
                return_text += i.text.strip() + "\n"
            except Exception as e:
                print(e)
                continue
        for i in problem_ul:
            try:
                return_text += i.text.strip() + "\n"
            except Exception as e:
                print(e)
                continue
        return_text += "\n\n **IN** \n"
        for i in input_description:
            try:
                return_text += i.text.strip() + "\n"
            except Exception as e:
                print(e)
                continue
        return_text += "\n\n **OUT** \n"
        for i in output_description:
            try:
                return_text += i.text.strip() + "\n"
            except Exception as e:
                print(e)
                continue
        return_text += "\n\n **EXAMPLE** \n"
        for i in range(len(sample_i)):
            return_text += f"## IN {i + 1} ###" + "\n"
            try:
                return_text += sample_i[i].text.strip() + "\n"
            except Exception as e:
                print(e)
                continue
            return_text += f"## OUT {i + 1} ###" + "\n"
            try:
                return_text += sample_o[i].text.strip() + "\n"
            except Exception as e:
                print(e)
                continue

        return return_text
    else:
        print(response.status_code)
