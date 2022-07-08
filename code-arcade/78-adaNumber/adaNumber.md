<p>Consider two following representations of a non-negative integer:</p>
<ol>
<li>A simple decimal integer, constructed of a non-empty sequence of digits from <code>0</code> to <code>9</code>;</li>
<li>An integer with at least one digit in a base from <code>2</code> to <code>16</code> (inclusive), enclosed between <code>#</code> characters, and preceded by the base, which can only be a number between <code>2</code> and <code>16</code> in the first representation. For digits from <code>10</code> to <code>15</code> characters <code>a</code>, <code>b</code>, ..., <code>f</code> and <code>A</code>, <code>B</code>, ..., <code>F</code> are used.</li>
</ol>
<p>Additionally, both representations may contain <em>underscore</em> (<code>_</code>) characters; they are used only as separators for improving legibility of numbers and can be ignored while processing a number.</p>
<p>Your task is to determine whether the given string is a valid integer representation.</p>
<p><i>Note: this is how integer numbers are represented in the programming language Ada.</i></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>line = "123_456_789"</code>, the output should be<br />
<code>solution(line) = true</code>;</li>
<li>For <code>line = "16#123abc#"</code>, the output should be<br />
<code>solution(line) = true</code>;</li>
<li>For <code>line = "10#123abc#"</code>, the output should be<br />
<code>solution(line) = false</code>;</li>
<li>For <code>line = "10#10#123ABC#"</code>, the output should be<br />
<code>solution(line) = false</code>;</li>
<li>For <code>line = "10#0#"</code>, the output should be<br />
<code>solution(line) = true</code>;</li>
<li>For <code>line = "10##"</code>, the output should be<br />
<code>solution(line) = false</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string line</strong></p>
<p>A non-empty string.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ line.length ≤ 30</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>line</code> is a valid integer representation, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
