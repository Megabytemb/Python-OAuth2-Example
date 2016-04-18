#Python OAuth2 Example

This is a simple litte example on how to do App Engine Authentication using OpenID/OAuth2


##Domain-wide Authentication
To allow all users within a Google Apps domain to access this App
without being prompted for approval:
1. Go to Security > Show More > Advanced Settings > Manage Client API Access
2. The Client Name is the Client-id from your Client_Secrets.json
3. You only need the `email` scope
4. click _Authorize_

##Initial Struggles
`access_type='online'` means alot. Without it, this app will ask for a refresh token, which require Offline access, which then breaks the seemless login experience for the User.

Setting `access_type` to `online` ensures that the token is only valid for the current user session.


###Todo
Improve this Doco