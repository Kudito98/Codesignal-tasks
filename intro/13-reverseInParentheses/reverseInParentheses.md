<p>Write a function that reverses characters in (possibly nested) parentheses in the input string.</p>
<p>Input strings will always be well-formed with matching <code>()</code>s.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>inputString = "(bar)"</code>, the output should be<br />
<code>solution(inputString) = "rab"</code>;</li>
<li>For <code>inputString = "foo(bar)baz"</code>, the output should be<br />
<code>solution(inputString) = "foorabbaz"</code>;</li>
<li>For <code>inputString = "foo(bar)baz(blim)"</code>, the output should be<br />
<code>solution(inputString) = "foorabbazmilb"</code>;</li>
<li>For <code>inputString = "foo(bar(baz))blim"</code>, the output should be<br />
<code>solution(inputString) = "foobazrabblim"</code>.<br />
Because <code>"foo(bar(baz))blim"</code> becomes <code>"foo(barzab)blim"</code> and then <code>"foobazrabblim"</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string inputString</strong></p>
<p>A string consisting of lowercase English letters and the characters <code>(</code> and <code>)</code>. It is guaranteed that all parentheses in <code>inputString</code> form a <a href="keyword://regular-bracket-sequence" target="_blank">regular bracket sequence</a>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ inputString.length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Return <code>inputString</code>, with all the characters that were in parentheses reversed.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
