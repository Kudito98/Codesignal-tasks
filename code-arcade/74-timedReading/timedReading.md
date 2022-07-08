<p>Timed Reading is an educational tool used in many schools to improve and advance reading skills. A young elementary student has just finished his very first timed reading exercise. Unfortunately he's not a very good reader yet, so whenever he encountered a word longer than <code>maxLength</code>, he simply skipped it and read on.</p>
<p>Help the teacher figure out how many words the boy has read by calculating the number of words in the <code>text</code> he has read, no longer than <code>maxLength</code>.<br />
Formally, a word is a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>maxLength = 4</code> and<br />
<code>text = "The Fox asked the stork, 'How is the soup?'"</code>,<br />
the output should be<br />
<code>solution(maxLength, text) = 7</code>.</p>
<p>The boy has read the following words: <code>"The", "Fox", "the", "How", "is", "the", "soup"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer maxLength</strong></p>
<p>A positive integer, the maximum length of the word the boy can read.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ maxLength ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string text</strong></p>
<p>A non-empty string of English letters and punctuation marks.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ text.length ≤ 110</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of words the boy has read.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
