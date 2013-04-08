<select id="{{ id }}"
% if multiple:
    name="{{ name }}[]"
    multiple="multiple"
    data-bind="foreach: medium_options, attr: { size: medium_options().length }"
% else:
    data-bind="foreach: medium_options"
    name="{{ name }}"
% end
>
  <option data-bind="value: id, text: text" />
</select>
