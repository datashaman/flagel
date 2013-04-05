<ul data-bind="foreach: short_options">
  <li>
    <input type="checkbox" data-bind="attr: { id: '{{id}}-' + id }, value: id" name="{{ name }}[]" />
    <label class="inline" data-bind="attr: { for: '{{id}}-' + id }, text: text" />
  </li>
</ul>
