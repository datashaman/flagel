<select id="{{ id }}"
% if multiple:
    name="{{ name}}[]"
    multiple="multiple"
% else:
    name="{{ name}}"
% end
>
    %for text, value in options:
        <option value="{{ value }}">{{ text }}</option>
    %end
</select>
