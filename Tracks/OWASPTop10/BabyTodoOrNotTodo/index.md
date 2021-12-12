1. From `schema.sql`, we know the todo table has flag
2. From `routes.py`, we know the /api/list/all is where we want to exploit
3. From `utils.py`, we know there is a loophole in auth process
4. Pasting URL like `http://178.62.123.156:32533/api/list/all/?secret=CCE20eA0cA34ac7` on browser to exploit 
