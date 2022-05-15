def accident_generator(camera_id, is_accident, type_of_accident, time_video, time_real):
    return {
        'camera_id': camera_id,
        'is_accident': is_accident,
        'type': type_of_accident,
        'time_video': time_video,
        'time_real': time_real
    }


def get_mock_data():
    data = []
    data.append(accident_generator(
        1, True, 'full', '1:01:01', '2022-06-15 1:01:01'
    ))
    data.append(accident_generator(
        1, False, 'unloaded', '3:03:03', '2022-06-15 3:03:03'
    ))

    data.append(accident_generator(
        2, True, 'overloaded', '5:07:11', '2022-05-11 5:07:11'
    ))
    data.append(accident_generator(
        2, False, 'unloaded', '13:06:23', '2022-05-11 13:06:23'
    ))

    data.append(accident_generator(
        3, True, 'near_full_can', '6:12:21', '2022-05-25 6:12:21'
    ))
    data.append(accident_generator(
        3, False, 'unloaded', '7:03:03', '2022-05-25 7:03:03'
    ))

    data.append(accident_generator(
        4, True, 'near_empty_can', '9:04:01', '2022-06-11 9:04:01'
    ))
    data.append(accident_generator(
        4, False, 'unloaded', '12:43:03', '2022-06-11 12:43:03'
    ))

    return data
