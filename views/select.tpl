<select id="{{ id }}" name="{{ name }}">
    %for text, value in options:
        <option value="{{ value }}">{{ text }}</option>
    %end
</select>
