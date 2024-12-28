from uuid import UUID
from fastapi import FastAPI

from bank_account.v5_use_eventsourcing_package.application.account import AccountApplication

tags_metadata = [
    {
        "name": "Account Management",
        # "description": "Manage account(create, deposit, withdraw, close)",
    },
    {
        "name": "Projection",
        # "description": "get accounts report.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

accounts = AccountApplication()


@app.get("/accounts/{account_id}", tags=["Accounting"])
def get_account(account_id: UUID):
    try:
        account = accounts.get_account(account_id)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return account


@app.post("/accounts", tags=["Accounting"])
def create_account(full_name: str):
    try:
        account_id = accounts.create_account(full_name)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return account_id


@app.post("/account/{account_id}/deposit", tags=["Accounting"])
def deposit_funds(account_id: UUID, amount: float):
    try:
        accounts.deposit(
            account_id=account_id,
            amount=amount,
        )
        account = accounts.get_account(account_id)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return account


@app.post("/account/{account_id}/withdraw", tags=["Accounting"])
def withdraw_funds(account_id: UUID, amount: float):
    try:
        accounts.withdraw(
            account_id=account_id,
            amount=amount,
        )
        account = accounts.get_account(account_id)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return account


# @app.post("/account/{account_id}/transfer")
# def transfer_funds(account_id: UUID, to_account_id: UUID, amount: Decimal):
#     try:
#         accounts.transfer_funds(
#             debit_account_id=account_id,
#             credit_account_id=to_account_id,
#             amount=amount,
#         )
#         account = accounts.get_account(account_id)
#     except Exception as e:
#         return {"error": e.__class__.__name__}
#     return account


# @app.post("/account/{account_id}/overdraft")
# def set_overdraft_limit(account_id: UUID, limit: Decimal):
#     try:
#         accounts.set_overdraft_limit(
#             account_id=account_id,
#             overdraft_limit=limit,
#         )
#         account = accounts.get_account(account_id)
#     except Exception as e:
#         return {"error": e.__class__.__name__}
#     return account


@app.post("/account/{account_id}/close", tags=["Accounting"])
def close_account(account_id: UUID):
    try:
        accounts.block_account(account_id)
        account = accounts.get_account(account_id)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return account


@app.get("/{account_id}/balance", tags=["Projection"])
async def get_account_balance(account_id: UUID):
    return {"balance": accounts.balance_projection.account_balances[account_id]}


@app.get("/total_balance/", tags=["Projection"])
async def get_total_balance():
    return {"balance": accounts.balance_projection.total_balance}


@app.get("/balances", tags=["Projection"])
def get_all_account_balance():
    return {"balance": accounts.balance_projection.account_balances}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="localhost", port=5000, log_level="debug", reload=True)



