import requests
import urllib3
import json
from behave import when
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from auth_vars import tokens, res, sc_id
from utils import generate_random_chars, post_request

VERMILLION_URL = 'https://localhost'
SEARCH_ENDPOINT = '/search'
SCROLL_ENDPOINT = '/search/scroll'
url = VERMILLION_URL + SCROLL_ENDPOINT

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@when('A geo-spatial query is initiated with scroll field in body')
def step_impl(context):
    context.type = 'geospatial-scroll'

    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "10s",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with scroll field and a token')
def step_impl(context):
    params = (
        ('token', tokens["master"]),

    )
    payload = {
        "id":
            res[1],
        "scroll_duration": "10m",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, params, json.dumps(payload), context)


@when('A geo-spatial query is initiated with scroll field not a string')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": 10,
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m"

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with extraneous parameters')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll": "1m",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with invalid scroll value')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "m",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with scroll value equal to 0')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "0m",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with scroll value greater than 1hr')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "2hr",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m"

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with scroll value greater than 60m')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "100m",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m"

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with scroll value greater than 3600s')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "4000s",
        "size": 500,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with response size as string')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "10s",
        "size": "500",
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with invalid response size integer')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "10s",
        "size": 1.1,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with response size greater than 10000')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "10s",
        "size": 100000,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('A geo-spatial query is initiated with response size less than 0')
def step_impl(context):
    payload = {
        "id":
            "rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/rs.varanasi.iudx.org.in/varanasi-swm-vehicles/varanasi-swm-vehicles-live.public",
        "scroll_duration": "10s",
        "size": -123,
        "geo_distance": {
            "coordinates": [82.9739, 25.3176],
            "distance": "10000m",

        }
    }
    url = VERMILLION_URL + SEARCH_ENDPOINT
    post_request(url, "", json.dumps(payload), context)


@when('The scroll search query without body')
def step_impl(context):
    # payload = {
    #     # "scroll_id": sc_id,
    #     # "scroll_duration": "5s"
    #
    # }
    post_request(url, "", None, context)


@when('The scroll search query with invalid json body')
def step_impl(context):
    payload = {
        "scroll_id": sc_id,
        "scroll_duration": True

    }
    post_request(url, "", payload, context)


@when('The scroll search query without scroll duration')
def step_impl(context):
    payload = {
        "scroll_id": sc_id

    }
    post_request(url, "", json.dumps(payload), context)


@when('The scroll search query without scroll id')
def step_impl(context):
    payload = {
        "scroll_duration": "5s"

    }
    post_request(url, "", json.dumps(payload), context)


@when('The scroll search query with empty body')
def step_impl(context):
    payload = {

    }
    post_request(url, "", json.dumps(payload), context)


@when('The scroll search query with token')
def step_impl(context):
    params = (
        ('token', tokens["master"]),

    )
    payload = {
        "scroll_id": sc_id,
        "scroll_duration": "5s"

    }
    post_request(url, params, json.dumps(payload), context)


@when('The scroll search query with invalid token')
def step_impl(context):
    params = (
        ('token', generate_random_chars()),
    )
    payload = {
        "scroll_id": sc_id,
        "scroll_duration": "5s"

    }
    post_request(url, params, json.dumps(payload), context)


@when('The scroll search query with extraneous parameters')
def step_impl(context):
    # params = (
    #     ('token', generate_random_chars()),
    # )
    payload = {
        "scroll_id": sc_id,
        "scroll_duration": "5s",
        "xyz": 123

    }
    post_request(url, "", json.dumps(payload), context)


@when('The scroll search query is initiated')
def step_impl(context):
    context.type = 'scroll-search'
    payload = {
        "scroll_id": sc_id,
        "scroll_duration": "5s"

    }
    r = requests.post(url=VERMILLION_URL + SCROLL_ENDPOINT,
                      headers={'content-type': 'application/json'},
                      data=json.dumps(payload),
                      verify=False)

    context.response = r.json()['hits']

