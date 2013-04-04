<select id="{{ id }}"
% if multiple:
    name="{{ name}}[]"
    multiple="multiple"
% else:
    name="{{ name}}"
% end
>
    %for option in options:
        <option value="{{ option.id }}">{{ option.label }}</option>
    %end
</select>
