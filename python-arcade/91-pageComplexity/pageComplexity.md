<p>You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the complexity of the main page of your site. In order to measure the complexity of the page, you need to find a set of all tags located on the deepest level of a tree correponsing to HTML document. Given a valid HTML <code>document</code>, find all distinct tags located on the deepest level.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For<br />
<code>document = "&lt;!DOCTYPE html&gt;&lt;html&gt;  &lt;body&gt;    &lt;h1&gt;The best heading ever&lt;/h1&gt;    &lt;p&gt;The worst paragraph ever.&lt;/p&gt;  &lt;/body&gt;&lt;/html&gt;"</code><br />
the output should be<br />
<code>solution(document) = ["h1", "p"]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string document</strong></p>
<p>Correct HTML document.</p>
<p><em>Guaranteed constraints:</em><br />
<code>10 ≤ document.length ≤ 900</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>List of all distinct tags on the deepest level sorted <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographically</a>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
