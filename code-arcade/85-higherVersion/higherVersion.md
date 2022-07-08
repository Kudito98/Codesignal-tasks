<p>Given two version strings composed of several non-negative decimal fields separated by periods (<code>"."</code>), both strings contain equal number of numeric fields. Return <code>true</code> if the first version is higher than the second version and <code>false</code> otherwise.</p>
<p>The syntax follows the regular <em>semver</em> ordering rules:</p>
<pre><code>1.0.5 &lt; 1.1.0 &lt; 1.1.5 &lt; 1.1.10 &lt; 1.2.0 &lt; 1.2.2
&lt; 1.2.10 &lt; 1.10.2 &lt; 2.0.0 &lt; 10.0.0
</code></pre>
<p>There are no leading zeros in any of the numeric fields, i.e. you do not have to handle inputs like <code>100.020.003</code> (it would instead be given as <code>100.20.3</code>).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>ver1 = "1.2.2"</code> and <code>ver2 = "1.2.0"</code>, the output should be<br />
<code>solution(ver1, ver2) = true</code>;</li>
<li>For <code>ver1 = "1.0.5"</code> and <code>ver2 = "1.1.0"</code>, the output should be<br />
<code>solution(ver1, ver2) = false</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string ver1</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ ver1.length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] string ver2</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ ver2.length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
