define ['jquery', 'knockout'], ($, ko) ->
    () ->
        model = @

        @loggedInUser = ko.observable()

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

        $.get '/auth/status', (status) ->
            model.loggedInUser(status.email)

            navigator.id.watch
                loggedInUser: status.email
                onlogin: (assertion) ->
                    $.post('/auth/login', assertion: assertion)
                        .done (status) ->
                            model.loggedInUser(status.email)
                        .fail (jqXHR, textStatus, errorThrown) ->
                            console.log('Signin failed: ' + errorThrown)
                            navigator.id.logout()
                onlogout: ->
                    $.post('/auth/logout')
                        .done ->
                            model.loggedInUser(null)
                        .fail (jqXHR, textStatus, errorThrown) ->
                            console.log('Signout failed: ' + errorThrown)

            $('#auth').show()

        return
