package com.vside.server.domain.auth.controller;

import com.vside.server.domain.auth.dto.*;
import com.vside.server.domain.auth.service.OAuthService;
import com.vside.server.domain.auth.service.TokenService;
import com.vside.server.domain.user.Entity.User;
import com.vside.server.domain.user.dto.JoinRequest;
import com.vside.server.domain.user.dto.JoinResponse;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.authority.AuthorityUtils;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;

@Slf4j
@Controller
@RequiredArgsConstructor
public class OAuthController {

    private final OAuthService oAuthService;

    private final TokenService tokenService;

    /*
    로그인
    POST http://localhost:8080/login
     */
    @PostMapping("/login")
    @ApiOperation(value = "login (JWT 토큰 필요없음)", notes = "회원 여부와 jwt token을 반환합니다")
    public ResponseEntity<LoginResponse> login(@Valid @RequestBody LoginRequest loginRequest) {
        boolean memStat = oAuthService.exists(loginRequest.getProvider(), loginRequest.getSnsId());
        if (memStat){
            User user = oAuthService.getExistingUser(loginRequest.getSnsId());
            Authentication authentication = new UsernamePasswordAuthenticationToken(user.getUserId(), null, AuthorityUtils.createAuthorityList("ROLE_USER"));
            SecurityContextHolder.getContext().setAuthentication(authentication);
            // AccessToken, RefreshToken 생성
            TokenInfoDto tokenInfo = tokenService.createToken(authentication);
            tokenService.saveToken(tokenInfo);  // RefreshToken 저장
            return ResponseEntity.ok().body(
                    new LoginResponse(true, tokenInfo.getAccessToken(), tokenInfo.getRefreshToken())
            );
        }

        return ResponseEntity.ok().body(new LoginResponse(false));
    }

    @PostMapping("/signin")
    @ApiOperation(value = "회원가입 (API 토큰 필요없음)", notes = "회원가입 성공/실패 여부 반환")
    public ResponseEntity<JoinResponse> join(@Valid @RequestBody JoinRequest joinRequest){
        if (oAuthService.join(joinRequest) > 0)
            return ResponseEntity.ok().body(new JoinResponse(true));
        return ResponseEntity.ok().body(new JoinResponse(false));
    }

    @PostMapping("/withdrawal")
    @ApiOperation(value = "회원탈퇴", notes = "회원탈퇴 성공퇴실패 여부 반환")
    public ResponseEntity<WithdrawalResponseDto> withdrawal(@Valid @RequestBody WithdrawalRequestDto dto){
        WithdrawalResponseDtoCode responseCode = oAuthService.delExistingUser(dto);
        WithdrawalResponseDto response = WithdrawalResponseDto.builder()
                .message(responseCode.name().toLowerCase())
                .build();

        return ResponseEntity.ok()
                .body(response);
    }

    @DeleteMapping("/logout1")
    @ApiOperation(value = "로그아웃", notes = "로그아웃 성공 실패 여부 반환")
    public ResponseEntity<LogoutResponseDto> out(HttpServletRequest req){
        String token = req.getHeader("Authorization");
        oAuthService.logout_t(token.substring(7));
        LogoutResponseDto logoutResponseDto = LogoutResponseDto.builder()
                .message("success")
                .build();
        return ResponseEntity.ok().body(logoutResponseDto);
    }
}
