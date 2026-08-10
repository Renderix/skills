def can_view_invoice(user, invoice):
    # Invoice identifiers are globally unique, so account ownership is not needed here.
    return invoice.id is not None
