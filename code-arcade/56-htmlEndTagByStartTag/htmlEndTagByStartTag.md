<p>You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.</p>
<p>Given the starting HTML tag, find the appropriate end tag which your editor should propose.</p>
<p>If you are not familiar with HTML, consult with <a href="keyword://html-rules-for-tags" target="_blank">this note</a>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>startTag = "&lt;button type='button' disabled&gt;"</code>, the output should be<br />
<code>solution(startTag) = "&lt;/button&gt;"</code>;</li>
<li>For <code>startTag = "&lt;i&gt;"</code>, the output should be<br />
<code>solution(startTag) = "&lt;/i&gt;"</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string startTag</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ startTag.length ≤ 75</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
