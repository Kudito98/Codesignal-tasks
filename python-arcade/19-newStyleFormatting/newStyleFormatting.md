<p>You came to work in a big company as a Senior Python Developer. Unfortunately your team members seem to be quite old-school: you can see old-style string formatting everywhere in the code, which is not too cool. You tried to force the team members to start using the new style formatting, but it looks like it will take some time to persuade them: old habits die hard, especially in old-school programmers.</p>
<p>To show your colleagues that the new style formatting is not that different from the old style, you decided to implement a function that will turn the old-style syntax into a new one. Implement a function that will turn the old-style string formating <code>s</code> into a new one so that the following two strings have the same meaning:</p>
<ul>
<li><code>s % (*args)</code></li>
<li><code>s.format(*args)</code></li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>s = "We expect the %f%% growth this week"</code>, the output should be<br />
<code>solution(s) = "We expect the {}% growth this week"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p>A correct old-style formatting string. It is guaranteed that each <code>%</code> sign in it is always followed either by a correct conversion type or by another <code>'%'</code> sign (see <a href="https://docs.python.org/2/library/string.html#format-specification-mini-language" target="_blank">this</a> for reference). It is also guaranteed that it doesn't contain curly brackets (<code>'{'</code> or <code>'}'</code>).</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ s.length ≤ 70</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A new-style formatting string without positional indices.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
