<select id="{{ id }}"
% if multiple:
    name="{{ name }}[]"
    multiple="multiple"
    data-bind="select2: { width: '100%' }, foreach: medium_options, attr: { size: medium_options().length }"
% else:
    data-bind="select2: { width: '100%' }, foreach: medium_options, attr: { size: medium_options().length }"
    name="{{ name }}"
% end
>
  <option data-bind="value: id, text: text" />
</select>
