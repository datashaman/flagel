define ['jquery', 'knockout'], ($, ko) ->
    () ->
        model = @
        model.loggedInUser = ko.observable()

        $.get 'http://localhost:8080/auth/status', (status) ->
            model.loggedInUser(status.email)
            $('#auth').show()

            $('#sign-in').click ->
                navigator.id.request
                    siteName: 'Flagel'
                    termsOfService: '/#tos'
                    privacyPolicy: '/#privacy'
                    returnTo: '/#welcome'
                    oncancel: ->
                        console.log('User refused')

            $('#sign-out').click ->
                navigator.id.logout()

            navigator.id.watch
                loggedInUser: model.loggedInUser()
                onlogin: (assertion) ->
                    $.post('http://localhost:8080/auth/login', assertion: assertion)
                        .done (status) ->
                            model.loggedInUser(status.email)
                        .fail (jqXHR, textStatus, errorThrown) ->
                            console.log('Signin failed: ' + errorThrown)
                            navigator.id.logout()
                onlogout: ->
                    $.post('http://localhost:8080/auth/logout')
                        .done ->
                            model.loggedInUser(null)
                        .fail (jqXHR, textStatus, errorThrown) ->
                            console.log('Signout failed: ' + errorThrown)

        return
