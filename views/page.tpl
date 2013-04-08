<form class="vertical">
    <ul class="tabs left">
    <li><a href="#tab-select">Select</a></li>
    </ul>

    <form>
    <div id="tab-select" class="tab-content grid flex">
        <div id="params">
        Short Point (&lt;= <output data-bind="text: short_point"></output>): <input type="range" data-bind="value: short_point" min="2" max="12" />
        Medium Point (&lt;= <output data-bind="text: medium_point"></output>): <input type="range" data-bind="value: medium_point" min="2" max="12" />
        </div>

        {{! select_content }}
    </div>
    </form>
</form>
%rebase layout title='Demo'
