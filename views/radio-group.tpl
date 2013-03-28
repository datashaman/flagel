% index = 0
% for text, value in options:
    % option_id = '%s-%s' % (id, value)
    <input type="radio" id="{{ option_id }}" name="{{ name }}" value="{{ value }}" />
    <label for="{{ option_id }}" class="inline">{{ text }}</label>
    % index += 1
    % if index < len(options):
    <br />
    % end
% end
