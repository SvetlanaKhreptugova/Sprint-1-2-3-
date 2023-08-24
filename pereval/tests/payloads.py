valid_pass_test_data = {
    "beauty_title": "Ullua",
    "title": "Ullua",
    "other_title": "Пхия",
    "connect": "",
    "add_time": "2023-07-26T20:39:36.764989Z",
    "user": {
        "first_name": "Gaga",
        "surname": "Past",
        "last_name": "Lady",
        "email": "mail1@yandex.ru",
        "phone": "19929394934"
    },
    "coords": {
        "latitude": 54.345,
        "longitude": 54.4534,
        "height": 600
    },
    "level": {
        "winter": "hard",
        "summer": "",
        "autumn": "",
        "spring": ""
    },
    "images": [
        {
            "id": 1,
            "data": "https://s.mediasalt.ru/cache/content/data/images/130/130083/original.jpg",
            "title": "foto1"
        }
    ],
    "status": "New"
}

missing_user_test_data = {
    'beauty_title': 'пер. ',
    'title': 'Пхия',
    'other_titles': 'Триев',
    'connect': '',
    'coords': {
        'height': 1200,
        'latitude': 45.3842,
        'longtitude': 7.1525
    },
    'level': {
        'winter': '',
        'summer': '1А',
        'autumn': '1А',
        'spring': ''
    },
    'images': [
        {
            'title': 'Седловина',
            'data': 'https://images.com/image1.jpg'
        },
        {
            'title': 'Подъём',
            'data': 'https://images.com/image2.jpg'
        }
    ]
}

missing_coords_test_data = {
    'beauty_title': 'пер. ',
    'title': 'Пхия',
    'other_titles': 'Триев',
    'connect': '',
    'level': {
        'winter': '',
        'summer': '1А',
        'autumn': '1А',
        'spring': ''
    },
    'images': [
        {
            'title': 'Седловина',
            'data': 'https://images.com/image1.jpg'
        },
        {
            'title': 'Подъём',
            'data': 'https://images.com/image2.jpg'
        }
    ]
}

missing_level_test_data = {
    'beauty_title': 'пер. ',
    'title': 'Пхия',
    'other_titles': 'Триев',
    'connect': '',
    'coords': {
        'height': 1200,
        'latitude': 45.3842,
        'longtitude': 7.1525
    },
    'images': [
        {
            'title': 'Седловина',
            'data': 'https://images.com/image1.jpg'
        },
        {
            'title': 'Подъём',
            'data': 'https://images.com/image2.jpg'
        }
    ]
}

missing_images_test_data = {
    'beauty_title': 'пер. ',
    'title': 'Пхия',
    'other_titles': 'Триев',
    'connect': '',
    'coords': {
        'height': 1200,
        'latitude': 45.3842,
        'longtitude': 7.1525
    },
    'level': {
        'winter': '',
        'summer': '1А',
        'autumn': '1А',
        'spring': ''
    }
}

patch_data = {
     "beauty_title": "Ullua",
    "title": "Ullua",
    "other_title": "Пхия",
    "connect": "",
    "add_time": "2023-07-26T20:39:36.764989Z",
    "user": {
        "first_name": "Gaga",
        "surname": "Past",
        "last_name": "Lady",
        "email": "mail1@yandex.ru",
        "phone": "19929394934"
    },
    "coords": {
        "latitude": 33.4423,
        "longitude": 43.4324,
        "height": 1000
    },
    "level": {
        "winter": "1A",
        "summer": "",
        "autumn": "",
        "spring": ""
    },
    "images": [
        {
            "id": 1,
            "data": "https://s.mediasalt.ru/cache/content/data/images/130/130083/original.jpg",
            "title": "foto1"
        }
    ],
    "status": "New"
}
