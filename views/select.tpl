<select id="{{ id }}"
  data-bind="foreach: medium_options"
% if multiple:
    name="{{ name }}[]"
    multiple="multiple"
% else:
    name="{{ name }}"
% end
>
  <option data-bind="value: id, text: text" />
</select>
