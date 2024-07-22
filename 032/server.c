//6. getpeername()
//server program
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#define PORT 8080
int main() {
 int sockfd, new_socket;
 struct sockaddr_in server_addr, client_addr;
 socklen_t addr_len = sizeof(client_addr);
 // Creating socket file descriptor
 if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
 perror("socket failed");
 exit(EXIT_FAILURE);
 }
 // Assigning IP and port
 server_addr.sin_family = AF_INET;
 server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
 server_addr.sin_port = htons(PORT);
 // Binding newly created socket to given IP and verification
 if (bind(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
 perror("bind failed");
 exit(EXIT_FAILURE);
 }
 // Listening for clients
 if (listen(sockfd, 5) == -1) {
 perror("listen");
 exit(EXIT_FAILURE);
 }
 printf("Server listening on port %d...\n", PORT);
 // Accepting incoming connections
 if ((new_socket = accept(sockfd, (struct sockaddr *)&client_addr, &addr_len)) == -1) {
 perror("accept");
 exit(EXIT_FAILURE);
 }
 // Getting peer name of the connected client
 if (getpeername(new_socket, (struct sockaddr *)&client_addr, &addr_len) == -1) {
 perror("getpeername");
 exit(EXIT_FAILURE);
 }
 printf("Client connected from %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));
 close(sockfd);
 return 0;
}
