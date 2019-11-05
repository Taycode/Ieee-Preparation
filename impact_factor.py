import json
a = {"publications": [
    {"publicationTitle" : "Letters on IEEEXtreme", "publicationNumber" : "1","articleCounts" : [
        {"year" : "2017","articleCount" : "3"},
        {"year" : "2018","articleCount" : "6"}
    ]},
    {"publicationTitle" : "Journal of 24 hours programing", "publicationNumber" : "2","articleCounts" : [
        {"year" : "2017","articleCount" : "1"}, {"year" : "2018","articleCount" : "4"}
    ]}
]}

#
# b = {"publisher": "IEEE","title": "Publication Title 1","contentType": "periodicals","ieeeCitationCount": "4","publicationNumber": "15","paperCitations": {
#     "ieee": [
#         {"order": "1","articleNumber" : "41","publicationNumber" : "4","year" : "2018","title": "Article 41"},
#         {"order": "2","articleNumber" : "109","publicationNumber" : "3","year" : "2015","title": "Article 109"},
#         {"order": "3","articleNumber" : "135","publicationNumber" : "1","year" : "2018","title": "Article 135"},
#         {"order": "4","articleNumber" : "97","publicationNumber" : "1","year" : "2016","title": "Article 97"},
#         {"order": "5","articleNumber" :"31","publicationNumber" : "1","year" : "2015","title": "Article 31"},
#         {"order": "6","articleNumber" : "89","publicationNumber" : "4","year" : "2018","title": "Article 89"},
#         {"order": "7","articleNumber" : "9","publicationNumber" : "4","year" : "2018","title": "Article 9"},
#         {"order": "8","articleNumber" : "26","publicationNumber" : "1","year" : "2015","title": "Article 26"},
#         {"order": "9","articleNumber" : "117","publicationNumber" : "1","year" : "2015","title": "Article 117"},
#         {"order": "10","articleNumber" : "35","publicationNumber" : "2","year" : "2019","title": "Article 35"},
#         {"order": "11","articleNumber" : "9","publicationNumber" : "2","year" : "2016","title": "Article 9"},
#         {"order": "12","articleNumber" : "61","publicationNumber" : "1","year" : "2017","title": "Article 61"},
#         {"order": "13","articleNumber" : "75","publicationNumber" : "3","year" : "2019","title": "Article 75"},
#         {"order": "14","articleNumber" : "25","publicationNumber" : "2","year" : "2019","title": "Article 25"},
#         {"order": "15","articleNumber" : "56","publicationNumber" : "3","year" : "2016","title": "Article 56"}]}}
#

def do_me_good(json_dict, pub_json_list):
    pub_num = json_dict["publicationNumber"]
    year = json_dict["year"]


def calculate_total_articles(json_dict):
    num = 0
    year_list = json_dict["articleCounts"]
    for year in year_list:
        if year["year"] == "2018" or year["year"] == "2017":
            num += int(year["articleCount"])
    return num


def calculate_total_amount_of_citations(json_dict, pub_num):
    data_list = json_dict["paperCitations"]["ieee"]
    num = 0
    for data in data_list:
        if data["publicationNumber"] == pub_num and (data["year"] == "2018" or data["year"] == "2017"):
            print(data)
            num += 1
    return num


def main(request, pub_data):

    total_num_of_articles = calculate_total_articles(pub_data)
    total_num_of_citations = calculate_total_amount_of_citations(request, pub_data["publicationNumber"])
    return {"total_cit": total_num_of_citations, "total_pub": total_num_of_articles}


if __name__ == '__main__':
    first_input = int(input())
    second_input = input()
    pub_list = []
    for publication in json.loads(second_input)["publications"]:
        pub_list.append(publication)

    count = 0
    total_cit = 0
    total_pub = 0
    while count < first_input - 1:
        my_input = input()
        res = main(json.loads(my_input), pub_list[0])
        total_cit += res["total_cit"]
        total_pub += res["total_pub"]
        count += 1
    print(total_cit/total_pub)
