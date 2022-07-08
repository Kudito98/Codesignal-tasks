<p>The World Wide Competitive Eating tournament is going to be held in your town, and you're the one who is responsible for keeping track of time. For the great finale, a large billboard of the given <code>width</code> will be installed on the main square, where the time of possibly new world record will be shown.</p>
<p>The track of time will be kept by a float number. It will be displayed on the board with the set precision <code>precision</code> with center alignment, and it is guaranteed that it will fit in the screen. Your task is to test the billboard. Given the time <code>t</code>, the <code>width</code> of the screen and the <code>precision</code> with which the time should be displayed, return a string that should be shown on the billboard.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>t = 3.1415</code>, <code>width = 10</code>, and <code>precision = 2</code>,<br />
the output should be</p>
<pre><code>solution(t, width, precision) = "   3.14   "
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] float t</strong></p>
<p>The time to be displayed on the billboard. It is guaranteed that <code>t</code> has at most <code>5</code> digits after the decimal point.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ t &lt; 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer width</strong></p>
<p>The width of the billboard. It is guaranteed that it's big enough to display the time <code>t</code> with the desired precision.</p>
<p>In case it's impossible to align the time perfectly in the center, left padding should be <code>1</code> whitespace character shorter than right padding.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ width ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer precision</strong></p>
<p>Precision with which the number should be displayed.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ precision ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A string of length <code>width</code> representing the time <code>t</code> as it will be displayed on the billboard.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
