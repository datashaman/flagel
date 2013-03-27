<ul id="{{ id }}">
%for text, value in options:
    <li><input type="checkbox" id="{{ '%s-%s' % (id, value) }}" value="{{ value }}" /> {{ text }}</li>
%end
</ul>
