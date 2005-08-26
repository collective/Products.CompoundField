##parameters=fieldname,size

context.Schema()[fieldname].resize(int(size),context)

return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])