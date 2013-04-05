<form class="vertical">
    <div id="params">
      Short Point: <input type="range" data-bind="value: short_point(), attr: { max: medium_point() - 1 }" min="2" />
      Medium Point: <input type="range" data-bind="value: medium_point(), attr: { min: short_point() + 1 }" />
    </div>

    <ul class="tabs left">
    <li><a href="#tab-select">Select</a></li>
    </ul>

    <form>
    <div id="tab-select" class="tab-content grid flex">
    {{! select_content }}
    </div>
    </form>
</form>
%rebase layout title='Demo'
