% index = 0
% for option in options:
    % option_id = '%s-%s' % (id, option.id)
    <input type="checkbox" id="{{ option_id }}" name="{{ name }}[]" value="{{ option.id }}" />
    <label for="{{ option_id }}" class="inline">{{ option.label }}</label>
    % index += 1
    % if index < len(options):
    <br />
    % end
% end
