def can_view_invoice(user, invoice):
    return user.account_id == invoice.account_id
