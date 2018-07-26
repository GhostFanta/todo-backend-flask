from alembic import op
import sqlalchemy as sa

import json

items_1 = [
    {
        'id': 1,
        'content': 'Define app structure',
        'isCompleted': 0,
    },
    {
        'id': 2,
        'content': 'Finish TodoList Page',
        'isCompleted': 0,
    },
    {
        'id': 3,
        'content': 'Finish TodoList',
        'isCompleted': 0,
    }

]

items_2 = [
    {
        'id': 1,
        'content': 'Add auth logic',
        'isCompleted': 0,
    },
    {
        'id': 2,
        'content': 'Add deployment scripts',
        'isCompleted': 0,
    },
]


def seed_data():
    target_table = sa.sql.table('todo_lists', sa.String)
    op.bulk_insert(
        target_table,
        [
            {'id': 1,
             'title': 'Release1',
             'createdtime': '2018-02-02',
             'lastmodifiedtime': '2018-02-02',
             'item': json.dumps(items_1)
             },
            {
                'title': 'Release2',
                'createdtime': '2018-02-05',
                'lastmodifiedtime': '2018-02-05',
                'item': json.dumps(items_2)
            },
        ]
    )


