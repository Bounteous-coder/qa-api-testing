# API Test Case Inventory

| ID | Title | Priority | Type | Expected Result |
| --- | --- | --- | --- | --- |
| TC-API-001 | Get users returns 200 | High | Positive | Response is 200 and array is returned |
| TC-API-002 | Users list non-empty | High | Positive | List contains at least one user |
| TC-API-003 | Users list has expected count | Medium | Positive | List count is 10 |
| TC-API-004 | User schema includes required fields | High | Positive | id, name, username, email, address, company are present |
| TC-API-005 | Get user by id returns 200 | High | Positive | /users/1 returns 200 |
| TC-API-006 | Selected user has valid email | Medium | Positive | /users/2 has email with '@' |
| TC-API-007 | Secondary user endpoint returns 200 | Medium | Positive | /users/5 returns 200 |
| TC-API-008 | Unknown user id 0 behavior | Medium | Negative | 404 or empty payload handled |
| TC-API-009 | Unknown user id 99999 behavior | Medium | Negative | 404 or empty payload handled |
| TC-API-010 | Another user email validation | Low | Positive | /users/7 has valid email |
| TC-API-011 | Get posts returns 200 | High | Positive | /posts returns 200 |
| TC-API-012 | Posts list non-empty | High | Positive | List contains 100 or more posts |
| TC-API-013 | Get single post returns 200 | High | Positive | /posts/1 returns 200 |
| TC-API-014 | Single post includes required fields | Medium | Positive | id, userId, title, body are present |
| TC-API-015 | Posts query by userId returns 200 | Medium | Positive | /posts?userId=1 returns 200 |
| TC-API-016 | Posts query by userId filters correctly | High | Positive | All records returned have userId=1 |
| TC-API-017 | Create post with valid payload | High | Positive | 201 with echoed payload and id |
| TC-API-018 | Unknown post id 0 behavior | Medium | Negative | 404 or empty payload handled |
| TC-API-019 | Unknown post id 99999 behavior | Medium | Negative | 404 or empty payload handled |
| TC-API-020 | Created post id type validation | Low | Positive | Created post contains numeric id |

Add remaining cases in Jira and link each to execution evidence.
