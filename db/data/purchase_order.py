import datetime
from decimal import Decimal

purchase_order = [   {   'agreed_delivery_date': '2022-11-09',
        'agreed_delivery_location_id': 6,
        'agreed_payment_date': '2022-11-07',
        'counterparty_id': 11,
        'created_at': datetime.datetime(2022, 11, 3, 14, 20, 52, 187000),
        'currency_id': 2,
        'item_code': 'ZDOI5EA',
        'item_quantity': 371,
        'item_unit_price': Decimal('361.39'),
        'last_updated': datetime.datetime(2022, 11, 3, 14, 20, 52, 187000),
        'purchase_order_id': 1,
        'staff_id': 12},
    {   'agreed_delivery_date': '2022-11-04',
        'agreed_delivery_location_id': 8,
        'agreed_payment_date': '2022-11-07',
        'counterparty_id': 17,
        'created_at': datetime.datetime(2022, 11, 3, 14, 20, 52, 186000),
        'currency_id': 2,
        'item_code': 'QLZLEXR',
        'item_quantity': 286,
        'item_unit_price': Decimal('199.04'),
        'last_updated': datetime.datetime(2022, 11, 3, 14, 20, 52, 186000),
        'purchase_order_id': 2,
        'staff_id': 20},
    {   'agreed_delivery_date': '2022-11-05',
        'agreed_delivery_location_id': 16,
        'agreed_payment_date': '2022-11-04',
        'counterparty_id': 15,
        'created_at': datetime.datetime(2022, 11, 3, 14, 20, 52, 187000),
        'currency_id': 2,
        'item_code': 'AN3D85L',
        'item_quantity': 839,
        'item_unit_price': Decimal('658.58'),
        'last_updated': datetime.datetime(2022, 11, 3, 14, 20, 52, 187000),
        'purchase_order_id': 3,
        'staff_id': 12},
    {   'agreed_delivery_date': '2022-11-10',
        'agreed_delivery_location_id': 2,
        'agreed_payment_date': '2022-11-05',
        'counterparty_id': 2,
        'created_at': datetime.datetime(2022, 11, 3, 14, 20, 52, 186000),
        'currency_id': 3,
        'item_code': 'I9MET53',
        'item_quantity': 316,
        'item_unit_price': Decimal('803.82'),
        'last_updated': datetime.datetime(2022, 11, 3, 14, 20, 52, 186000),
        'purchase_order_id': 5,
        'staff_id': 18},
    {   'agreed_delivery_date': '2022-12-03',
        'agreed_delivery_location_id': 11,
        'agreed_payment_date': '2022-12-03',
        'counterparty_id': 12,
        'created_at': datetime.datetime(2022, 11, 30, 8, 2, 10, 683000),
        'currency_id': 2,
        'item_code': 'QKQQ9IS',
        'item_quantity': 597,
        'item_unit_price': Decimal('714.89'),
        'last_updated': datetime.datetime(2022, 11, 30, 8, 2, 10, 683000),
        'purchase_order_id': 62,
        'staff_id': 13},
    {   'agreed_delivery_date': '2022-11-04',
        'agreed_delivery_location_id': 24,
        'agreed_payment_date': '2022-11-08',
        'counterparty_id': 5,
        'created_at': datetime.datetime(2022, 11, 4, 11, 59, 9, 990000),
        'currency_id': 2,
        'item_code': 'DAOECK5',
        'item_quantity': 926,
        'item_unit_price': Decimal('155.70'),
        'last_updated': datetime.datetime(2022, 11, 4, 11, 59, 9, 990000),
        'purchase_order_id': 6,
        'staff_id': 11},
    {   'agreed_delivery_date': '2022-11-10',
        'agreed_delivery_location_id': 7,
        'agreed_payment_date': '2022-11-07',
        'counterparty_id': 5,
        'created_at': datetime.datetime(2022, 11, 4, 12, 18, 9, 885000),
        'currency_id': 2,
        'item_code': 'PBF02WW',
        'item_quantity': 51,
        'item_unit_price': Decimal('909.87'),
        'last_updated': datetime.datetime(2022, 11, 4, 12, 18, 9, 885000),
        'purchase_order_id': 7,
        'staff_id': 20},
    {   'agreed_delivery_date': '2022-11-10',
        'agreed_delivery_location_id': 5,
        'agreed_payment_date': '2022-11-09',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 4, 18, 3, 10, 233000),
        'currency_id': 2,
        'item_code': '8R25O35',
        'item_quantity': 119,
        'item_unit_price': Decimal('782.15'),
        'last_updated': datetime.datetime(2022, 11, 4, 18, 3, 10, 233000),
        'purchase_order_id': 8,
        'staff_id': 15},
    {   'agreed_delivery_date': '2022-11-12',
        'agreed_delivery_location_id': 13,
        'agreed_payment_date': '2022-11-09',
        'counterparty_id': 10,
        'created_at': datetime.datetime(2022, 11, 7, 17, 6, 10, 294000),
        'currency_id': 2,
        'item_code': 'M9NO0XK',
        'item_quantity': 14,
        'item_unit_price': Decimal('695.86'),
        'last_updated': datetime.datetime(2022, 11, 7, 17, 6, 10, 294000),
        'purchase_order_id': 10,
        'staff_id': 3},
    {   'agreed_delivery_date': '2022-11-13',
        'agreed_delivery_location_id': 29,
        'agreed_payment_date': '2022-11-08',
        'counterparty_id': 4,
        'created_at': datetime.datetime(2022, 11, 7, 17, 36, 9, 898000),
        'currency_id': 3,
        'item_code': 'RRGNEG2',
        'item_quantity': 991,
        'item_unit_price': Decimal('225.64'),
        'last_updated': datetime.datetime(2022, 11, 7, 17, 36, 9, 898000),
        'purchase_order_id': 11,
        'staff_id': 15},
    {   'agreed_delivery_date': '2022-11-14',
        'agreed_delivery_location_id': 19,
        'agreed_payment_date': '2022-11-09',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 8, 15, 30, 10, 600000),
        'currency_id': 3,
        'item_code': 'M7DY4XU',
        'item_quantity': 850,
        'item_unit_price': Decimal('596.50'),
        'last_updated': datetime.datetime(2022, 11, 8, 15, 30, 10, 600000),
        'purchase_order_id': 13,
        'staff_id': 6},
    {   'agreed_delivery_date': '2022-11-11',
        'agreed_delivery_location_id': 25,
        'agreed_payment_date': '2022-11-11',
        'counterparty_id': 7,
        'created_at': datetime.datetime(2022, 11, 8, 17, 34, 9, 912000),
        'currency_id': 2,
        'item_code': 'LJDZX2T',
        'item_quantity': 582,
        'item_unit_price': Decimal('321.35'),
        'last_updated': datetime.datetime(2022, 11, 8, 17, 34, 9, 912000),
        'purchase_order_id': 14,
        'staff_id': 19},
    {   'agreed_delivery_date': '2022-11-14',
        'agreed_delivery_location_id': 6,
        'agreed_payment_date': '2022-11-09',
        'counterparty_id': 15,
        'created_at': datetime.datetime(2022, 11, 8, 18, 50, 10, 306000),
        'currency_id': 2,
        'item_code': '53FS4LJ',
        'item_quantity': 217,
        'item_unit_price': Decimal('616.20'),
        'last_updated': datetime.datetime(2022, 11, 8, 18, 50, 10, 306000),
        'purchase_order_id': 15,
        'staff_id': 7},
    {   'agreed_delivery_date': '2022-11-14',
        'agreed_delivery_location_id': 12,
        'agreed_payment_date': '2022-11-10',
        'counterparty_id': 17,
        'created_at': datetime.datetime(2022, 11, 9, 8, 41, 10, 654000),
        'currency_id': 3,
        'item_code': 'XTI9R6R',
        'item_quantity': 998,
        'item_unit_price': Decimal('93.43'),
        'last_updated': datetime.datetime(2022, 11, 9, 8, 41, 10, 654000),
        'purchase_order_id': 16,
        'staff_id': 13},
    {   'agreed_delivery_date': '2022-11-06',
        'agreed_delivery_location_id': 7,
        'agreed_payment_date': '2022-11-06',
        'counterparty_id': 17,
        'created_at': datetime.datetime(2022, 11, 3, 14, 20, 52, 187000),
        'currency_id': 2,
        'item_code': 'P4O34NV',
        'item_quantity': 720,
        'item_unit_price': Decimal('79.26'),
        'last_updated': datetime.datetime(2022, 11, 3, 14, 20, 52, 187000),
        'purchase_order_id': 4,
        'staff_id': 18},
    {   'agreed_delivery_date': '2022-11-14',
        'agreed_delivery_location_id': 6,
        'agreed_payment_date': '2022-11-15',
        'counterparty_id': 5,
        'created_at': datetime.datetime(2022, 11, 10, 13, 10, 10, 329000),
        'currency_id': 2,
        'item_code': 'TJXHSOW',
        'item_quantity': 987,
        'item_unit_price': Decimal('647.40'),
        'last_updated': datetime.datetime(2022, 11, 10, 13, 10, 10, 329000),
        'purchase_order_id': 17,
        'staff_id': 20},
    {   'agreed_delivery_date': '2022-11-14',
        'agreed_delivery_location_id': 23,
        'agreed_payment_date': '2022-11-11',
        'counterparty_id': 6,
        'created_at': datetime.datetime(2022, 11, 10, 13, 16, 9, 911000),
        'currency_id': 3,
        'item_code': 'DFNGPZ1',
        'item_quantity': 342,
        'item_unit_price': Decimal('675.04'),
        'last_updated': datetime.datetime(2022, 11, 10, 13, 16, 9, 911000),
        'purchase_order_id': 18,
        'staff_id': 6},
    {   'agreed_delivery_date': '2022-11-11',
        'agreed_delivery_location_id': 14,
        'agreed_payment_date': '2022-11-11',
        'counterparty_id': 4,
        'created_at': datetime.datetime(2022, 11, 10, 15, 49, 10, 108000),
        'currency_id': 2,
        'item_code': 'IQ6Z9YA',
        'item_quantity': 621,
        'item_unit_price': Decimal('472.45'),
        'last_updated': datetime.datetime(2022, 11, 10, 15, 49, 10, 108000),
        'purchase_order_id': 19,
        'staff_id': 11},
    {   'agreed_delivery_date': '2022-11-17',
        'agreed_delivery_location_id': 22,
        'agreed_payment_date': '2022-11-16',
        'counterparty_id': 15,
        'created_at': datetime.datetime(2022, 11, 11, 11, 18, 10, 421000),
        'currency_id': 3,
        'item_code': 'GAU0VXO',
        'item_quantity': 848,
        'item_unit_price': Decimal('145.77'),
        'last_updated': datetime.datetime(2022, 11, 11, 11, 18, 10, 421000),
        'purchase_order_id': 20,
        'staff_id': 8},
    {   'agreed_delivery_date': '2022-11-14',
        'agreed_delivery_location_id': 30,
        'agreed_payment_date': '2022-11-17',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 11, 14, 25, 10, 197000),
        'currency_id': 2,
        'item_code': 'T67H77C',
        'item_quantity': 385,
        'item_unit_price': Decimal('593.00'),
        'last_updated': datetime.datetime(2022, 11, 11, 14, 25, 10, 197000),
        'purchase_order_id': 21,
        'staff_id': 4},
    {   'agreed_delivery_date': '2022-11-15',
        'agreed_delivery_location_id': 28,
        'agreed_payment_date': '2022-11-17',
        'counterparty_id': 7,
        'created_at': datetime.datetime(2022, 11, 11, 17, 40, 10, 497000),
        'currency_id': 3,
        'item_code': 'GEMNFRI',
        'item_quantity': 606,
        'item_unit_price': Decimal('476.82'),
        'last_updated': datetime.datetime(2022, 11, 11, 17, 40, 10, 497000),
        'purchase_order_id': 22,
        'staff_id': 7},
    {   'agreed_delivery_date': '2022-11-19',
        'agreed_delivery_location_id': 2,
        'agreed_payment_date': '2022-11-15',
        'counterparty_id': 18,
        'created_at': datetime.datetime(2022, 11, 14, 8, 12, 10, 313000),
        'currency_id': 2,
        'item_code': 'CZM6IOU',
        'item_quantity': 227,
        'item_unit_price': Decimal('668.72'),
        'last_updated': datetime.datetime(2022, 11, 14, 8, 12, 10, 313000),
        'purchase_order_id': 23,
        'staff_id': 16},
    {   'agreed_delivery_date': '2022-11-18',
        'agreed_delivery_location_id': 24,
        'agreed_payment_date': '2022-11-15',
        'counterparty_id': 10,
        'created_at': datetime.datetime(2022, 11, 14, 18, 25, 10, 356000),
        'currency_id': 3,
        'item_code': 'NYBKXGX',
        'item_quantity': 708,
        'item_unit_price': Decimal('484.26'),
        'last_updated': datetime.datetime(2022, 11, 14, 18, 25, 10, 356000),
        'purchase_order_id': 24,
        'staff_id': 13},
    {   'agreed_delivery_date': '2022-11-15',
        'agreed_delivery_location_id': 30,
        'agreed_payment_date': '2022-11-17',
        'counterparty_id': 10,
        'created_at': datetime.datetime(2022, 11, 15, 8, 46, 9, 877000),
        'currency_id': 2,
        'item_code': '8LZ0CE6',
        'item_quantity': 844,
        'item_unit_price': Decimal('343.39'),
        'last_updated': datetime.datetime(2022, 11, 15, 8, 46, 9, 877000),
        'purchase_order_id': 26,
        'staff_id': 3},
    {   'agreed_delivery_date': '2022-11-19',
        'agreed_delivery_location_id': 17,
        'agreed_payment_date': '2022-11-20',
        'counterparty_id': 19,
        'created_at': datetime.datetime(2022, 11, 15, 15, 39, 10, 617000),
        'currency_id': 3,
        'item_code': 'WBVSMXH',
        'item_quantity': 737,
        'item_unit_price': Decimal('957.81'),
        'last_updated': datetime.datetime(2022, 11, 15, 15, 39, 10, 617000),
        'purchase_order_id': 27,
        'staff_id': 17},
    {   'agreed_delivery_date': '2022-11-19',
        'agreed_delivery_location_id': 16,
        'agreed_payment_date': '2022-11-17',
        'counterparty_id': 19,
        'created_at': datetime.datetime(2022, 11, 15, 17, 12, 10, 531000),
        'currency_id': 3,
        'item_code': '5MWHVVC',
        'item_quantity': 89,
        'item_unit_price': Decimal('272.25'),
        'last_updated': datetime.datetime(2022, 11, 15, 17, 12, 10, 531000),
        'purchase_order_id': 28,
        'staff_id': 9},
    {   'agreed_delivery_date': '2022-11-20',
        'agreed_delivery_location_id': 13,
        'agreed_payment_date': '2022-11-21',
        'counterparty_id': 13,
        'created_at': datetime.datetime(2022, 11, 17, 16, 34, 10, 296000),
        'currency_id': 2,
        'item_code': 'BZ9844U',
        'item_quantity': 703,
        'item_unit_price': Decimal('779.25'),
        'last_updated': datetime.datetime(2022, 11, 17, 16, 34, 10, 296000),
        'purchase_order_id': 30,
        'staff_id': 7},
    {   'agreed_delivery_date': '2022-11-24',
        'agreed_delivery_location_id': 10,
        'agreed_payment_date': '2022-11-22',
        'counterparty_id': 7,
        'created_at': datetime.datetime(2022, 11, 17, 17, 1, 10, 91000),
        'currency_id': 3,
        'item_code': 'S9R4LED',
        'item_quantity': 391,
        'item_unit_price': Decimal('200.76'),
        'last_updated': datetime.datetime(2022, 11, 17, 17, 1, 10, 91000),
        'purchase_order_id': 31,
        'staff_id': 3},
    {   'agreed_delivery_date': '2022-11-21',
        'agreed_delivery_location_id': 2,
        'agreed_payment_date': '2022-11-23',
        'counterparty_id': 11,
        'created_at': datetime.datetime(2022, 11, 18, 13, 52, 10, 512000),
        'currency_id': 3,
        'item_code': '2KCHQ3S',
        'item_quantity': 818,
        'item_unit_price': Decimal('980.82'),
        'last_updated': datetime.datetime(2022, 11, 18, 13, 52, 10, 512000),
        'purchase_order_id': 32,
        'staff_id': 18},
    {   'agreed_delivery_date': '2022-11-22',
        'agreed_delivery_location_id': 29,
        'agreed_payment_date': '2022-11-19',
        'counterparty_id': 19,
        'created_at': datetime.datetime(2022, 11, 18, 16, 54, 10, 339000),
        'currency_id': 3,
        'item_code': '2V1R1Z9',
        'item_quantity': 867,
        'item_unit_price': Decimal('354.00'),
        'last_updated': datetime.datetime(2022, 11, 18, 16, 54, 10, 339000),
        'purchase_order_id': 34,
        'staff_id': 15},
    {   'agreed_delivery_date': '2022-11-21',
        'agreed_delivery_location_id': 23,
        'agreed_payment_date': '2022-11-24',
        'counterparty_id': 14,
        'created_at': datetime.datetime(2022, 11, 21, 8, 50, 10, 292000),
        'currency_id': 3,
        'item_code': 'MASCUUC',
        'item_quantity': 682,
        'item_unit_price': Decimal('30.45'),
        'last_updated': datetime.datetime(2022, 11, 21, 8, 50, 10, 292000),
        'purchase_order_id': 35,
        'staff_id': 13},
    {   'agreed_delivery_date': '2022-11-25',
        'agreed_delivery_location_id': 29,
        'agreed_payment_date': '2022-11-22',
        'counterparty_id': 4,
        'created_at': datetime.datetime(2022, 11, 21, 14, 51, 10, 476000),
        'currency_id': 3,
        'item_code': 'QWPK0F3',
        'item_quantity': 525,
        'item_unit_price': Decimal('99.92'),
        'last_updated': datetime.datetime(2022, 11, 21, 14, 51, 10, 476000),
        'purchase_order_id': 36,
        'staff_id': 9},
    {   'agreed_delivery_date': '2022-11-24',
        'agreed_delivery_location_id': 3,
        'agreed_payment_date': '2022-11-25',
        'counterparty_id': 19,
        'created_at': datetime.datetime(2022, 11, 21, 17, 40, 10, 151000),
        'currency_id': 2,
        'item_code': 'AVTOJ6F',
        'item_quantity': 902,
        'item_unit_price': Decimal('336.79'),
        'last_updated': datetime.datetime(2022, 11, 21, 17, 40, 10, 151000),
        'purchase_order_id': 37,
        'staff_id': 19},
    {   'agreed_delivery_date': '2022-11-27',
        'agreed_delivery_location_id': 29,
        'agreed_payment_date': '2022-11-24',
        'counterparty_id': 2,
        'created_at': datetime.datetime(2022, 11, 22, 10, 40, 10, 213000),
        'currency_id': 3,
        'item_code': 'Q09PCAI',
        'item_quantity': 965,
        'item_unit_price': Decimal('977.67'),
        'last_updated': datetime.datetime(2022, 11, 22, 10, 40, 10, 213000),
        'purchase_order_id': 38,
        'staff_id': 16},
    {   'agreed_delivery_date': '2022-11-22',
        'agreed_delivery_location_id': 14,
        'agreed_payment_date': '2022-11-24',
        'counterparty_id': 7,
        'created_at': datetime.datetime(2022, 11, 22, 13, 38, 10, 357000),
        'currency_id': 3,
        'item_code': 'WZ7AEP7',
        'item_quantity': 489,
        'item_unit_price': Decimal('180.52'),
        'last_updated': datetime.datetime(2022, 11, 22, 13, 38, 10, 357000),
        'purchase_order_id': 40,
        'staff_id': 5},
    {   'agreed_delivery_date': '2022-11-23',
        'agreed_delivery_location_id': 19,
        'agreed_payment_date': '2022-11-23',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 22, 17, 2, 10, 130000),
        'currency_id': 2,
        'item_code': '125IBOG',
        'item_quantity': 288,
        'item_unit_price': Decimal('894.07'),
        'last_updated': datetime.datetime(2022, 11, 22, 17, 2, 10, 130000),
        'purchase_order_id': 41,
        'staff_id': 4},
    {   'agreed_delivery_date': '2022-11-22',
        'agreed_delivery_location_id': 12,
        'agreed_payment_date': '2022-11-28',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 22, 18, 41, 10, 413000),
        'currency_id': 3,
        'item_code': '192K94Q',
        'item_quantity': 154,
        'item_unit_price': Decimal('977.75'),
        'last_updated': datetime.datetime(2022, 11, 22, 18, 41, 10, 413000),
        'purchase_order_id': 42,
        'staff_id': 10},
    {   'agreed_delivery_date': '2022-11-23',
        'agreed_delivery_location_id': 2,
        'agreed_payment_date': '2022-11-28',
        'counterparty_id': 15,
        'created_at': datetime.datetime(2022, 11, 23, 10, 55, 10, 588000),
        'currency_id': 3,
        'item_code': 'ERKM497',
        'item_quantity': 865,
        'item_unit_price': Decimal('343.27'),
        'last_updated': datetime.datetime(2022, 11, 23, 10, 55, 10, 588000),
        'purchase_order_id': 43,
        'staff_id': 3},
    {   'agreed_delivery_date': '2022-11-28',
        'agreed_delivery_location_id': 29,
        'agreed_payment_date': '2022-11-25',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 24, 10, 5, 9, 988000),
        'currency_id': 3,
        'item_code': 'BJ74S77',
        'item_quantity': 273,
        'item_unit_price': Decimal('261.07'),
        'last_updated': datetime.datetime(2022, 11, 24, 10, 5, 9, 988000),
        'purchase_order_id': 44,
        'staff_id': 7},
    {   'agreed_delivery_date': '2022-11-27',
        'agreed_delivery_location_id': 8,
        'agreed_payment_date': '2022-11-24',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 24, 10, 7, 10, 9000),
        'currency_id': 3,
        'item_code': 'HWP01PM',
        'item_quantity': 714,
        'item_unit_price': Decimal('49.15'),
        'last_updated': datetime.datetime(2022, 11, 24, 10, 7, 10, 9000),
        'purchase_order_id': 45,
        'staff_id': 8},
    {   'agreed_delivery_date': '2022-11-27',
        'agreed_delivery_location_id': 20,
        'agreed_payment_date': '2022-11-28',
        'counterparty_id': 5,
        'created_at': datetime.datetime(2022, 11, 24, 12, 59, 10, 194000),
        'currency_id': 3,
        'item_code': 'MNZGQ80',
        'item_quantity': 61,
        'item_unit_price': Decimal('346.91'),
        'last_updated': datetime.datetime(2022, 11, 24, 12, 59, 10, 194000),
        'purchase_order_id': 46,
        'staff_id': 20},
    {   'agreed_delivery_date': '2022-11-30',
        'agreed_delivery_location_id': 18,
        'agreed_payment_date': '2022-11-29',
        'counterparty_id': 19,
        'created_at': datetime.datetime(2022, 11, 24, 14, 24, 10, 180000),
        'currency_id': 2,
        'item_code': '9NSEYM2',
        'item_quantity': 287,
        'item_unit_price': Decimal('746.27'),
        'last_updated': datetime.datetime(2022, 11, 24, 14, 24, 10, 180000),
        'purchase_order_id': 47,
        'staff_id': 6},
    {   'agreed_delivery_date': '2022-11-30',
        'agreed_delivery_location_id': 8,
        'agreed_payment_date': '2022-11-25',
        'counterparty_id': 4,
        'created_at': datetime.datetime(2022, 11, 24, 16, 46, 10, 333000),
        'currency_id': 3,
        'item_code': 'AC6KJXU',
        'item_quantity': 129,
        'item_unit_price': Decimal('116.24'),
        'last_updated': datetime.datetime(2022, 11, 24, 16, 46, 10, 333000),
        'purchase_order_id': 48,
        'staff_id': 17},
    {   'agreed_delivery_date': '2022-11-30',
        'agreed_delivery_location_id': 24,
        'agreed_payment_date': '2022-11-26',
        'counterparty_id': 7,
        'created_at': datetime.datetime(2022, 11, 25, 10, 3, 10, 592000),
        'currency_id': 3,
        'item_code': 'LYOYVQI',
        'item_quantity': 248,
        'item_unit_price': Decimal('757.18'),
        'last_updated': datetime.datetime(2022, 11, 25, 10, 3, 10, 592000),
        'purchase_order_id': 49,
        'staff_id': 12},
    {   'agreed_delivery_date': '2022-11-28',
        'agreed_delivery_location_id': 6,
        'agreed_payment_date': '2022-11-29',
        'counterparty_id': 20,
        'created_at': datetime.datetime(2022, 11, 25, 12, 27, 10, 103000),
        'currency_id': 3,
        'item_code': 'UO837BJ',
        'item_quantity': 407,
        'item_unit_price': Decimal('419.45'),
        'last_updated': datetime.datetime(2022, 11, 25, 12, 27, 10, 103000),
        'purchase_order_id': 50,
        'staff_id': 16},
    {   'agreed_delivery_date': '2022-12-02',
        'agreed_delivery_location_id': 12,
        'agreed_payment_date': '2022-11-27',
        'counterparty_id': 3,
        'created_at': datetime.datetime(2022, 11, 25, 15, 26, 10, 298000),
        'currency_id': 3,
        'item_code': '49DELPD',
        'item_quantity': 976,
        'item_unit_price': Decimal('769.01'),
        'last_updated': datetime.datetime(2022, 11, 25, 15, 26, 10, 298000),
        'purchase_order_id': 51,
        'staff_id': 20},
    {   'agreed_delivery_date': '2022-12-04',
        'agreed_delivery_location_id': 13,
        'agreed_payment_date': '2022-11-29',
        'counterparty_id': 10,
        'created_at': datetime.datetime(2022, 11, 28, 10, 7, 10, 403000),
        'currency_id': 2,
        'item_code': '9YOXW3R',
        'item_quantity': 416,
        'item_unit_price': Decimal('431.19'),
        'last_updated': datetime.datetime(2022, 11, 28, 10, 7, 10, 403000),
        'purchase_order_id': 53,
        'staff_id': 6},
    {   'agreed_delivery_date': '2022-12-05',
        'agreed_delivery_location_id': 2,
        'agreed_payment_date': '2022-12-02',
        'counterparty_id': 6,
        'created_at': datetime.datetime(2022, 11, 28, 13, 38, 10, 234000),
        'currency_id': 3,
        'item_code': 'G7NZQQP',
        'item_quantity': 884,
        'item_unit_price': Decimal('455.39'),
        'last_updated': datetime.datetime(2022, 11, 28, 13, 38, 10, 234000),
        'purchase_order_id': 54,
        'staff_id': 14},
    {   'agreed_delivery_date': '2022-11-30',
        'agreed_delivery_location_id': 18,
        'agreed_payment_date': '2022-12-04',
        'counterparty_id': 4,
        'created_at': datetime.datetime(2022, 11, 28, 17, 20, 10, 500000),
        'currency_id': 3,
        'item_code': 'QXJRI5A',
        'item_quantity': 356,
        'item_unit_price': Decimal('319.48'),
        'last_updated': datetime.datetime(2022, 11, 28, 17, 20, 10, 500000),
        'purchase_order_id': 55,
        'staff_id': 20},
    {   'agreed_delivery_date': '2022-12-03',
        'agreed_delivery_location_id': 23,
        'agreed_payment_date': '2022-12-03',
        'counterparty_id': 12,
        'created_at': datetime.datetime(2022, 11, 29, 10, 24, 10, 405000),
        'currency_id': 3,
        'item_code': 'C0X781W',
        'item_quantity': 333,
        'item_unit_price': Decimal('490.10'),
        'last_updated': datetime.datetime(2022, 11, 29, 10, 24, 10, 405000),
        'purchase_order_id': 56,
        'staff_id': 3}]